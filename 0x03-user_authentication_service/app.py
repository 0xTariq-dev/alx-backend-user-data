#!/usr/bin/env python3
""" A module for the Flask applicatiopn server """
from flask import Flask, jsonify, request, abort
from flask_cors import CORS
from auth import Auth


app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)
AUTH = Auth()


@app.route('/')
def home():
    """ The home route for the server """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'])
def users():
    """ The users route for the server """
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
