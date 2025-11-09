
# Recreate all templates with updated branding for FREE version

# index.html
index_html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Voice Bridge FREE - Real-Time Speech Translation</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
        <div class="container">
            <a class="navbar-brand" href="/">🌉 Voice Bridge <span class="badge bg-success">FREE</span></a>
            <div class="navbar-nav ms-auto">
                <a class="nav-link" href="/login">Login</a>
                <a class="nav-link" href="/register">Register</a>
            </div>
        </div>
    </nav>

    <div class="hero-section">
        <div class="container text-center">
            <h1 class="display-3 mb-4">Break Language Barriers</h1>
            <p class="lead mb-3">Real-time voice translation for seamless communication</p>
            <p class="lead mb-5">✅ 100% FREE • NO Payment Required • NO API Keys Needed</p>
            <div class="d-flex justify-content-center gap-3">
                <a href="/register" class="btn btn-primary btn-lg">Get Started FREE</a>
                <a href="/login" class="btn btn-outline-light btn-lg">Sign In</a>
            </div>
        </div>
    </div>

    <div class="container py-5">
        <div class="row g-4">
            <div class="col-md-4">
                <div class="card h-100 text-center">
                    <div class="card-body">
                        <div class="feature-icon mb-3">🎤</div>
                        <h3>Real-Time Translation</h3>
                        <p>Speak naturally and hear instant translations in your preferred language</p>
                    </div>
                </div>
            </div>
            <div class="col-md-4">
                <div class="card h-100 text-center">
                    <div class="card-body">
                        <div class="feature-icon mb-3">💰</div>
                        <h3>100% FREE</h3>
                        <p>No payment, no API keys, no credit card required. Forever free!</p>
                    </div>
                </div>
            </div>
            <div class="col-md-4">
                <div class="card h-100 text-center">
                    <div class="card-body">
                        <div class="feature-icon mb-3">🌍</div>
                        <h3>Multi-Language</h3>
                        <p>Support for 100+ languages with high-quality voice synthesis</p>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <footer class="bg-dark text-white text-center py-4 mt-5">
        <p>&copy; 2025 Voice Bridge FREE. Breaking barriers through free technology.</p>
        <p class="small">No payment ever required • Completely free forever</p>
    </footer>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>'''

# login.html
login_html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login - Voice Bridge FREE</title>
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
                        <h2 class="text-center mb-4">Login</h2>
                        <form id="loginForm">
                            <div class="mb-3">
                                <label for="email" class="form-label">Email</label>
                                <input type="email" class="form-control" id="email" required>
                            </div>
                            <div class="mb-3">
                                <label for="password" class="form-label">Password</label>
                                <input type="password" class="form-control" id="password" required>
                            </div>
                            <button type="submit" class="btn btn-primary w-100">Login</button>
                        </form>
                        <div id="message" class="mt-3"></div>
                        <p class="text-center mt-3">
                            Don't have an account? <a href="/register">Register FREE</a>
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

# Save templates
templates = [
    ('index.html', index_html),
    ('login.html', login_html),
]

for filename, content in templates:
    with open(f"{base_dir}/templates/{filename}", 'w') as f:
        f.write(content)

print("✅ Created index.html and login.html for FREE version")
