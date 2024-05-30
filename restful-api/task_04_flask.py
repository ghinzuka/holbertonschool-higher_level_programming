#!/usr/bin/python3
from flask import Flask
from flask import jsonify
from flask import request

users = {
    "Baptiste": {"name": "Baptiste", "age": 32, "city": "ayguemorte_les_graves"},
    "Nicolas": {"name": "Nicolas", "age": 28, "city": "Bordeaux"},
    "Matthieu": {"name": "Matthieu", "age": 26, "city": "Saint_denis_de_pile"},
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
		return jsonify(user)

@app.route("/add_user", methods=["POST"])
def add_user():
    new_user = request.get_json()
    username = new_user.get("username")
    users[username] = {
        "name": new_user.get("name"),
        "age": new_user.get("age"),
        "city": new_user.get("city")
    }
    return jsonify({"message": "User added", "user": users[username]})

if __name__ == "__main__": app.run()
