from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'supersecretjwtkey'

auth = HTTPBasicAuth()
jwt = JWTManager(app)

# Sample users dictionary with hashed passwords
users = {
    "user1": {"username": "user1", "password": generate_password_hash("password1"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password2"), "role": "admin"}
}

@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        return user

@auth.error_handler
def auth_error(status):
    return '', 401

@app.route('/basic-protected')
@auth.login_required
def basic_protected_route():
    return "Basic Auth: Access Granted"

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    user = users.get(username)

    if not user or not check_password_hash(user['password'], password):
        return "Bad username or password", 401

    access_token = create_access_token(identity={'username': username, 'role': user['role']})
    return jsonify(access_token=access_token)

@app.route('/jwt-protected')
@jwt_required()
def jwt_protected_route():
    return "JWT Auth: Access Granted", 200

@app.route('/admin-only')
@jwt_required()
def admin_only_route():
    current_user = get_jwt_identity()
    if current_user['role'] != 'admin':
        return "You do not have access to this route.", 403
    return "Admin Access: Granted", 200

# Custom Error Handlers for JWT errors
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return "Missing or invalid token", 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return "Invalid token", 401

@jwt.expired_token_loader
def handle_expired_token_error(err):
    return "Token has expired", 401

@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return "Token has been revoked", 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return "Fresh token required", 401

if __name__ == '__main__':
    app.run(debug=True)
