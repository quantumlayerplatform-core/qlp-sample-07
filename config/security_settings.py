from flask import Flask
from flask_cors import CORS
from flask_wtf.csrf import CSRFProtect
from flask_jwt_extended import JWTManager

def configure_security(app: Flask):
    # Configure CORS for handling Cross-Origin Resource Sharing
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    # Set up CSRF protection
    csrf = CSRFProtect()
    csrf.init_app(app)

    # Initialize JWT Manager for handling JWT authentication
    jwt = JWTManager(app)

    # Configure secure HTTP headers
    @app.after_request
    def set_secure_headers(response):
        response.headers['X-Frame-Options'] = 'SAMEORIGIN'
        response.headers['X-Content-Type-Options'] = 'nosniff'
        response.headers['X-XSS-Protection'] = '1; mode=block'
        response.headers['Strict-Transport-Security'] = 'max-age=63072000; includeSubDomains'
        response.headers['Content-Security-Policy'] = "default-src 'self'"
        return response

# Example usage:
# app = Flask(__name__)
# configure_security(app)