#!/usr/bin/env python3
""" Module for session authentication routes
"""
from os import getenv
from api.v1.views import app_views
from flask import request, jsonify, abort
from models.user import User


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def auth_session_login() -> str:
    """ POST /auth_session/login
    """
    not_found = jsonify({"error": "no user found for this email"})
    email = request.form.get('email')
    if not email or email == "":
        return jsonify({"error": "email missing"}), 400
    password = request.form.get('password')
    if not password or password == "":
        return jsonify({"error": "password missing"}), 400
    try:
        users = User.search({'email': email})
    except Exception:
        return not_found, 404
    if users is None or len(users) == 0:
        return not_found, 404
    user = users[0]
    if user.is_valid_password(password):
        from api.v1.app import auth
        session_id = auth.create_session(user.id)
        session_name = getenv('SESSION_NAME')
        response = jsonify(user.to_json())
        response.set_cookie(session_name, session_id)
        return response
    return jsonify({"error": "wrong password"}), 401
