from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['JWT_SECRET_KEY'] = 'supersecretjwtkey'

auth = HTTPBasicAuth()
jwt = JWTManager(app)

# Sample users dictionary
users = {
    "user1": {"username": "user1", "password": generate_password_hash("password1"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password2"), "role": "admin"}
}

@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        return user

@app.route('/')
def public_route():
    return jsonify({"message": "This is a public route."})

@app.route('/basic-protected')
@auth.login_required
def basic_protected_route():
    return jsonify({"message": "Basic Auth: Access Granted"})

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    user = users.get(username)

    if not user or not check_password_hash(user['password'], password):
        return jsonify({"message": "Bad username or password"}), 401

    access_token = create_access_token(identity={'username': username, 'role': user['role']})
    return jsonify(access_token=access_token)

@app.route('/jwt-protected')
@jwt_required()
def jwt_protected_route():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

if __name__ == '__main__':
    app.run(debug=True)