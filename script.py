
# Update app.py to remove Google Cloud dependency and use free libraries
updated_app_py = '''"""
Voice Bridge - Real-Time Speech Translation Web Application
Main Flask application with WebRTC signaling and free API integration
"""

from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from flask_socketio import SocketIO, emit, join_room, leave_room
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import secrets
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex(16)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///voicebridge.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
socketio = SocketIO(app, cors_allowed_origins="*", max_http_buffer_size=10000000)

# Database Models
class User(db.Model):
    """User model for authentication"""
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    
    def __repr__(self):
        return f'<User {self.username}>'

class CallRoom(db.Model):
    """Call room model for peer connections"""
    __tablename__ = 'call_rooms'
    
    id = db.Column(db.Integer, primary_key=True)
    room_code = db.Column(db.String(20), unique=True, nullable=False)
    host_user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    is_active = db.Column(db.Boolean, default=True)
    
    def __repr__(self):
        return f'<CallRoom {self.room_code}>'

# Create database tables
with app.app_context():
    db.create_all()

# Routes
@app.route('/')
def index():
    """Landing page"""
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    """User registration"""
    if request.method == 'POST':
        data = request.get_json()
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        
        # Check if user exists
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return jsonify({'success': False, 'message': 'Email already registered'}), 400
        
        # Create new user
        hashed_password = generate_password_hash(password)
        new_user = User(username=username, email=email, password_hash=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        
        return jsonify({'success': True, 'message': 'Registration successful'})
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """User login"""
    if request.method == 'POST':
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')
        
        user = User.query.filter_by(email=email).first()
        
        if user and check_password_hash(user.password_hash, password):
            session['user_id'] = user.id
            session['username'] = user.username
            return jsonify({'success': True, 'message': 'Login successful'})
        
        return jsonify({'success': False, 'message': 'Invalid credentials'}), 401
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    """User logout"""
    session.clear()
    return redirect(url_for('index'))

@app.route('/dashboard')
def dashboard():
    """User dashboard"""
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html', username=session.get('username'))

@app.route('/create-room', methods=['POST'])
def create_room():
    """Create a new call room"""
    if 'user_id' not in session:
        return jsonify({'success': False, 'message': 'Unauthorized'}), 401
    
    # Generate unique room code
    room_code = secrets.token_urlsafe(8)
    user_id = session['user_id']
    
    # Create room in database
    new_room = CallRoom(room_code=room_code, host_user_id=user_id)
    db.session.add(new_room)
    db.session.commit()
    
    return jsonify({'success': True, 'room_code': room_code})

@app.route('/call/<room_code>')
def call_room(room_code):
    """Call room page"""
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    # Verify room exists
    room = CallRoom.query.filter_by(room_code=room_code).first()
    if not room:
        return "Room not found", 404
    
    return render_template('call.html', room_code=room_code, username=session.get('username'))

@app.route('/translate-audio', methods=['POST'])
def translate_audio():
    """Handle audio translation using free APIs"""
    try:
        from translation_service import FreeTranslationService
        import tempfile
        import base64
        
        audio_file = request.files.get('audio')
        source_lang = request.form.get('source_lang', 'en')
        target_lang = request.form.get('target_lang', 'es')
        
        if not audio_file:
            return jsonify({'success': False, 'message': 'No audio provided'}), 400
        
        # Save audio temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as temp_audio:
            audio_file.save(temp_audio.name)
            temp_path = temp_audio.name
        
        # Initialize translation service
        translator = FreeTranslationService()
        
        # Process translation
        result = translator.full_translation_pipeline(temp_path, source_lang, target_lang)
        
        # Clean up temp file
        os.unlink(temp_path)
        
        # Encode audio as base64 for transmission
        audio_b64 = base64.b64encode(result['audio']).decode('utf-8')
        
        return jsonify({
            'success': True,
            'transcript': result['transcript'],
            'translation': result['translation'],
            'audio': audio_b64
        })
        
    except Exception as e:
        print(f"Translation error: {e}")
        return jsonify({'success': False, 'message': str(e)}), 500

# WebRTC Signaling via SocketIO
@socketio.on('join')
def on_join(data):
    """Handle user joining a room"""
    room = data['room']
    username = data['username']
    join_room(room)
    emit('user-connected', {'username': username}, room=room, include_self=False)
    print(f"{username} joined room {room}")

@socketio.on('offer')
def on_offer(data):
    """Handle WebRTC offer"""
    room = data['room']
    emit('offer', data, room=room, include_self=False)

@socketio.on('answer')
def on_answer(data):
    """Handle WebRTC answer"""
    room = data['room']
    emit('answer', data, room=room, include_self=False)

@socketio.on('ice-candidate')
def on_ice_candidate(data):
    """Handle ICE candidate exchange"""
    room = data['room']
    emit('ice-candidate', data, room=room, include_self=False)

@socketio.on('audio-chunk')
def on_audio_chunk(data):
    """Handle audio chunk for translation"""
    room = data['room']
    emit('audio-chunk', data, room=room, include_self=False)

@socketio.on('leave')
def on_leave(data):
    """Handle user leaving a room"""
    room = data['room']
    username = data['username']
    leave_room(room)
    emit('user-disconnected', {'username': username}, room=room)
    print(f"{username} left room {room}")

@socketio.on('language-change')
def on_language_change(data):
    """Handle language preference change"""
    room = data['room']
    language = data['language']
    username = data['username']
    emit('language-updated', {'username': username, 'language': language}, room=room, include_self=False)

if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0', port=5000)
'''

with open(f"{base_dir}/app.py", 'w') as f:
    f.write(updated_app_py)

print("✅ app.py updated to use FREE translation APIs!")
