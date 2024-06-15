#!/usr/bin/env python3
""" Auth module for the User authentication service"""

import bcrypt


def _hash_password(password: str) -> str:
    """ Returns a hashed password """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
