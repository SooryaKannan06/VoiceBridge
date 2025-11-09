# 🌉 Voice Bridge - FREE VERSION (No Payment Required!)

Voice Bridge is a **completely FREE** Python-based web application for real-time voice translation. No API keys, no Google Cloud account, no payment needed!

## ✨ What Makes This FREE?

This version uses **100% free libraries**:
- ✅ **SpeechRecognition** - Google's free speech recognition
- ✅ **googletrans** - Free Google Translate API
- ✅ **gTTS** - Free Google Text-to-Speech
- ✅ **No API keys required!**
- ✅ **No credit card needed!**
- ✅ **No payment ever!**

## 🚀 Quick Start (5 Minutes!)

### 1. Extract and Navigate
```bash
cd voice-bridge-free
```

### 2. Install Python Dependencies
```bash
# Create virtual environment (recommended)
python -m venv venv

# Activate it
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install all FREE libraries
pip install -r requirements.txt
```

### 3. Initialize Database
```bash
python -c "from app import app, db; app.app_context().push(); db.create_all()"
```

### 4. Run the App!
```bash
python app.py
```

Visit **http://localhost:5000** and start translating! 🎉

## 📱 How to Use

1. **Register** - Create a free account
2. **Login** - Sign in to your account
3. **Create Room** - Click "Create New Call Room" to get a room code
4. **Share Code** - Send the code to someone you want to call
5. **Join Call** - Both enter the room and allow microphone access
6. **Select Languages**:
   - Set "Your Language" (what you speak)
   - Set "Translate To" (what you want to hear)
7. **Start Talking** - Speak naturally and hear real-time translation!

## 🌍 Supported Languages (100% Free!)

- 🇬🇧 English
- 🇪🇸 Spanish
- 🇫🇷 French
- 🇩🇪 German
- 🇮🇳 Hindi
- 🇨🇳 Chinese
- 🇯🇵 Japanese
- 🇸🇦 Arabic
- 🇧🇷 Portuguese
- 🇷🇺 Russian
- 🇮🇹 Italian
- 🇰🇷 Korean
- And 100+ more!

## 🔧 Technical Details

### FREE APIs Used:
1. **Speech Recognition**: Uses Google's free speech-to-text service
2. **Translation**: googletrans library (reverse-engineered Google Translate)
3. **Text-to-Speech**: gTTS (Google Text-to-Speech free API)

### Architecture:
- **Backend**: Python Flask
- **Frontend**: HTML/CSS/JavaScript + Bootstrap
- **Real-time**: WebRTC + Socket.IO
- **Database**: SQLite (no setup needed)

## ⚠️ Limitations of Free Version

- **Rate Limits**: Google may throttle if you make too many requests
- **Voice Quality**: Good but not as premium as paid APIs
- **Internet Required**: All processing happens online
- **No Guarantees**: Free APIs can change without notice

For production use with high volume, consider upgrading to paid APIs.

## 🐛 Troubleshooting

### "No module named 'speech_recognition'"
```bash
pip install SpeechRecognition
```

### "Microphone not working"
- Allow microphone access in browser
- Use HTTPS (some browsers require it)
- Check browser console for errors

### "googletrans not working"
```bash
pip install googletrans==4.0.0rc1
```

### PyAudio Installation Issues

**Windows:**
```bash
pip install pipwin
pipwin install pyaudio
```

**Mac:**
```bash
brew install portaudio
pip install pyaudio
```

**Linux:**
```bash
sudo apt-get install python3-pyaudio
pip install pyaudio
```

## 📁 Project Structure

```
voice-bridge-free/
├── app.py                    # Main Flask app (uses FREE APIs)
├── translation_service.py    # FREE translation logic
├── requirements.txt          # Only free dependencies
├── README.md                 # This file
├── templates/                # HTML pages
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   └── call.html
└── static/                   # CSS & JavaScript
    ├── css/style.css
    └── js/
        ├── auth.js
        ├── dashboard.js
        └── webrtc.js
```

## 🎯 Features

✅ Real-time bidirectional translation  
✅ Secure user authentication  
✅ Room-based calling with codes  
✅ 100+ language support  
✅ Responsive modern UI  
✅ WebRTC peer-to-peer calls  
✅ **Completely FREE - No payment ever!**

## 🔒 Privacy & Security

- Passwords are hashed (not stored in plain text)
- Peer-to-peer calls (audio doesn't go through server)
- Session-based authentication
- All data stays on your machine (SQLite database)

## 🚀 Future Enhancements

- Offline translation (downloaded models)
- Group calls (3+ people)
- Call recording
- Mobile app version
- Video translation support

## 💡 Tips for Best Results

1. **Speak Clearly** - Better recognition
2. **Reduce Background Noise** - Use headphones
3. **Good Internet** - Faster translation
4. **Chrome/Firefox** - Best browser support
5. **HTTPS** - Use for production deployment

## 📞 Support

Having issues? Check:
1. All dependencies installed: `pip list`
2. Microphone permissions granted
3. Internet connection active
4. Python 3.8+ installed: `python --version`

## ⭐ Why This Project?

Breaking language barriers should be **accessible to everyone**, not just those who can afford expensive APIs. This project proves you can build powerful real-time translation without spending a cent!

## 📄 License

Free to use for personal and educational purposes!

---

**Built with ❤️ - Making communication accessible to all!**

**Remember: NO PAYMENT, NO API KEYS, COMPLETELY FREE! 🎉**
