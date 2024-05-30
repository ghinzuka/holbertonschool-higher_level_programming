#!/usr/bin/python3
from flask import Flask
from flask import jsonify
from flask import request

users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"},
}


app = Flask(__name__)
@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/data")
def data():
    usernames = list(users.keys())
    return jsonify(usernames)

@app.route("/status")
def status():
    return "OK"

@app.route("/users/<username>")
def user(username):
	user = users.get(username)
	if user:
		user["username"] = username
		return jsonify(user)
	else:
		return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods=["POST"])
def add_user():
    new_user = request.get_json()
    if not new_user:
        return jsonify({"error": "Invalid JSON data"}), 400
    username = new_user.get("username")
    if username in users:
        return jsonify({"error": "Username already exists"}), 409
    try:
        users[username] = {
            "name": new_user.get("name"),
            "age": new_user.get("age"),
            "city": new_user.get("city")
        }
        return jsonify({"message": "User added", "user": users[username]}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__": app.run()
