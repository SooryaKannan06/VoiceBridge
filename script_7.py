
# Create remaining templates - register, dashboard, call

register_html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Register - Voice Bridge FREE</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
        <div class="container">
            <a class="navbar-brand" href="/">🌉 Voice Bridge <span class="badge bg-success">FREE</span></a>
        </div>
    </nav>

    <div class="container mt-5">
        <div class="row justify-content-center">
            <div class="col-md-5">
                <div class="card shadow">
                    <div class="card-body p-5">
                        <h2 class="text-center mb-4">Register FREE</h2>
                        <p class="text-center text-muted mb-4">✅ No payment required</p>
                        <form id="registerForm">
                            <div class="mb-3">
                                <label for="username" class="form-label">Username</label>
                                <input type="text" class="form-control" id="username" required>
                            </div>
                            <div class="mb-3">
                                <label for="email" class="form-label">Email</label>
                                <input type="email" class="form-control" id="email" required>
                            </div>
                            <div class="mb-3">
                                <label for="password" class="form-label">Password</label>
                                <input type="password" class="form-control" id="password" required>
                            </div>
                            <button type="submit" class="btn btn-primary w-100">Register FREE</button>
                        </form>
                        <div id="message" class="mt-3"></div>
                        <p class="text-center mt-3">
                            Already have an account? <a href="/login">Login</a>
                        </p>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    <script src="{{ url_for('static', filename='js/auth.js') }}"></script>
</body>
</html>'''

dashboard_html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard - Voice Bridge FREE</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
        <div class="container">
            <a class="navbar-brand" href="/">🌉 Voice Bridge <span class="badge bg-success">FREE</span></a>
            <div class="navbar-nav ms-auto">
                <span class="navbar-text me-3">Welcome, {{ username }}!</span>
                <a class="nav-link" href="/logout">Logout</a>
            </div>
        </div>
    </nav>

    <div class="container mt-5">
        <div class="row">
            <div class="col-md-6 mx-auto">
                <div class="card shadow">
                    <div class="card-body p-5">
                        <h2 class="text-center mb-4">Start a Voice Call</h2>
                        <p class="text-center text-success mb-4">✅ Completely FREE • No limits</p>
                        
                        <div class="mb-4">
                            <button id="createRoomBtn" class="btn btn-primary btn-lg w-100">
                                🎤 Create New Call Room
                            </button>
                        </div>

                        <div id="roomCodeDisplay" class="alert alert-success d-none">
                            <h5>Your Room Code:</h5>
                            <h3 id="roomCodeText" class="text-center"></h3>
                            <p class="text-center mb-0">Share this code with others to join your call</p>
                            <button id="joinRoomBtn" class="btn btn-success w-100 mt-3">Join Room</button>
                        </div>

                        <hr class="my-4">

                        <div class="mb-3">
                            <h5>Join Existing Room</h5>
                            <div class="input-group">
                                <input type="text" id="joinCode" class="form-control" placeholder="Enter room code">
                                <button id="joinExistingBtn" class="btn btn-outline-primary">Join</button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    <script src="{{ url_for('static', filename='js/dashboard.js') }}"></script>
</body>
</html>'''

call_html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Call - Voice Bridge FREE</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
        <div class="container-fluid">
            <a class="navbar-brand" href="/">🌉 Voice Bridge <span class="badge bg-success">FREE</span></a>
            <span class="navbar-text text-white">Room: {{ room_code }}</span>
        </div>
    </nav>

    <div class="container-fluid mt-4">
        <div class="row">
            <div class="col-md-9">
                <div class="card shadow">
                    <div class="card-body text-center p-5">
                        <h3 id="connectionStatus" class="mb-4">Connecting...</h3>
                        
                        <div class="call-controls mb-4">
                            <button id="micBtn" class="btn btn-primary btn-lg mx-2">
                                🎤 Mute
                            </button>
                            <button id="endCallBtn" class="btn btn-danger btn-lg mx-2">
                                📞 End Call
                            </button>
                        </div>

                        <div id="remoteAudio"></div>
                        
                        <div class="mt-4">
                            <h5>Translation Status</h5>
                            <div id="translationStatus" class="alert alert-info">
                                ✅ Ready to translate (100% FREE!)
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <div class="col-md-3">
                <div class="card shadow">
                    <div class="card-header bg-primary text-white">
                        <h5 class="mb-0">Settings</h5>
                    </div>
                    <div class="card-body">
                        <div class="mb-3">
                            <label class="form-label">Your Language</label>
                            <select id="myLanguage" class="form-select">
                                <option value="en-US">English</option>
                                <option value="es-ES">Spanish</option>
                                <option value="fr-FR">French</option>
                                <option value="de-DE">German</option>
                                <option value="hi-IN">Hindi</option>
                                <option value="zh-CN">Chinese</option>
                                <option value="ja-JP">Japanese</option>
                                <option value="ar-SA">Arabic</option>
                                <option value="pt-BR">Portuguese</option>
                                <option value="ru-RU">Russian</option>
                            </select>
                        </div>

                        <div class="mb-3">
                            <label class="form-label">Translate To</label>
                            <select id="translateTo" class="form-select">
                                <option value="en-US">English</option>
                                <option value="es-ES">Spanish</option>
                                <option value="fr-FR">French</option>
                                <option value="de-DE">German</option>
                                <option value="hi-IN">Hindi</option>
                                <option value="zh-CN">Chinese</option>
                                <option value="ja-JP">Japanese</option>
                                <option value="ar-SA">Arabic</option>
                                <option value="pt-BR">Portuguese</option>
                                <option value="ru-RU">Russian</option>
                            </select>
                        </div>

                        <hr>

                        <div class="mb-3">
                            <h6>Participants</h6>
                            <ul id="participantList" class="list-group">
                                <li class="list-group-item">{{ username }} (You)</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <script src="https://cdn.socket.io/4.5.4/socket.io.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    <script>
        const roomCode = "{{ room_code }}";
        const username = "{{ username }}";
    </script>
    <script src="{{ url_for('static', filename='js/webrtc.js') }}"></script>
</body>
</html>'''

# Save templates
templates = [
    ('register.html', register_html),
    ('dashboard.html', dashboard_html),
    ('call.html', call_html),
]

for filename, content in templates:
    with open(f"{base_dir}/templates/{filename}", 'w') as f:
        f.write(content)

print("✅ Created all remaining templates (register, dashboard, call)")
