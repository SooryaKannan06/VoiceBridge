
# Create all static files (CSS and JS)

# style.css
css_content = '''/* Voice Bridge FREE - Styles */

:root {
    --primary-color: #0066cc;
    --secondary-color: #00c896;
    --dark-color: #1a1a1a;
    --light-color: #f8f9fa;
    --success-color: #28a745;
}

body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    min-height: 100vh;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}

.hero-section {
    padding: 100px 0;
    color: white;
}

.feature-icon {
    font-size: 3rem;
}

.card {
    border: none;
    border-radius: 15px;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.card:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 30px rgba(0,0,0,0.2);
}

.btn-primary {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    border: none;
    padding: 12px 30px;
    border-radius: 25px;
    font-weight: 600;
    transition: all 0.3s ease;
}

.btn-primary:hover {
    transform: scale(1.05);
    box-shadow: 0 5px 20px rgba(102, 126, 234, 0.4);
}

.navbar-brand {
    font-size: 1.5rem;
    font-weight: bold;
}

.badge.bg-success {
    font-size: 0.7rem;
    vertical-align: super;
}

.call-controls button {
    border-radius: 50px;
    padding: 15px 30px;
    font-size: 1.1rem;
}

#connectionStatus {
    color: var(--primary-color);
    font-weight: 600;
}

.alert {
    border-radius: 10px;
}

.form-control, .form-select {
    border-radius: 10px;
    padding: 12px;
}

.shadow {
    box-shadow: 0 10px 40px rgba(0,0,0,0.1) !important;
}

footer {
    margin-top: auto;
}

/* Animations */
@keyframes pulse {
    0%, 100% {
        opacity: 1;
    }
    50% {
        opacity: 0.5;
    }
}

.pulse {
    animation: pulse 2s infinite;
}

/* Responsive */
@media (max-width: 768px) {
    .hero-section {
        padding: 60px 0;
    }
    
    .hero-section h1 {
        font-size: 2rem;
    }
    
    .call-controls button {
        margin: 5px 0;
        width: 100%;
    }
}'''

# auth.js
auth_js = '''// Authentication JavaScript

const loginForm = document.getElementById('loginForm');
if (loginForm) {
    loginForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const email = document.getElementById('email').value;
        const password = document.getElementById('password').value;
        const messageDiv = document.getElementById('message');
        
        try {
            const response = await fetch('/login', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ email, password })
            });
            
            const data = await response.json();
            
            if (data.success) {
                messageDiv.innerHTML = '<div class="alert alert-success">Login successful! Redirecting...</div>';
                setTimeout(() => {
                    window.location.href = '/dashboard';
                }, 1000);
            } else {
                messageDiv.innerHTML = `<div class="alert alert-danger">${data.message}</div>`;
            }
        } catch (error) {
            messageDiv.innerHTML = '<div class="alert alert-danger">Login failed. Please try again.</div>';
        }
    });
}

const registerForm = document.getElementById('registerForm');
if (registerForm) {
    registerForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const username = document.getElementById('username').value;
        const email = document.getElementById('email').value;
        const password = document.getElementById('password').value;
        const messageDiv = document.getElementById('message');
        
        try {
            const response = await fetch('/register', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ username, email, password })
            });
            
            const data = await response.json();
            
            if (data.success) {
                messageDiv.innerHTML = '<div class="alert alert-success">Registration successful! Redirecting to login...</div>';
                setTimeout(() => {
                    window.location.href = '/login';
                }, 1500);
            } else {
                messageDiv.innerHTML = `<div class="alert alert-danger">${data.message}</div>`;
            }
        } catch (error) {
            messageDiv.innerHTML = '<div class="alert alert-danger">Registration failed. Please try again.</div>';
        }
    });
}'''

# dashboard.js
dashboard_js = '''// Dashboard JavaScript

const createRoomBtn = document.getElementById('createRoomBtn');
const roomCodeDisplay = document.getElementById('roomCodeDisplay');
const roomCodeText = document.getElementById('roomCodeText');
const joinRoomBtn = document.getElementById('joinRoomBtn');
const joinExistingBtn = document.getElementById('joinExistingBtn');
const joinCodeInput = document.getElementById('joinCode');

createRoomBtn.addEventListener('click', async () => {
    try {
        const response = await fetch('/create-room', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            }
        });
        
        const data = await response.json();
        
        if (data.success) {
            roomCodeText.textContent = data.room_code;
            roomCodeDisplay.classList.remove('d-none');
            createRoomBtn.disabled = true;
        }
    } catch (error) {
        alert('Failed to create room. Please try again.');
    }
});

joinRoomBtn.addEventListener('click', () => {
    const code = roomCodeText.textContent;
    if (code) {
        window.location.href = `/call/${code}`;
    }
});

joinExistingBtn.addEventListener('click', () => {
    const code = joinCodeInput.value.trim();
    if (code) {
        window.location.href = `/call/${code}`;
    } else {
        alert('Please enter a room code');
    }
});

joinCodeInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        joinExistingBtn.click();
    }
});'''

# Save static files
static_files = [
    ('static/css/style.css', css_content),
    ('static/js/auth.js', auth_js),
    ('static/js/dashboard.js', dashboard_js),
]

for filepath, content in static_files:
    with open(f"{base_dir}/{filepath}", 'w') as f:
        f.write(content)

print("✅ Created CSS and JavaScript files (auth.js, dashboard.js)")
