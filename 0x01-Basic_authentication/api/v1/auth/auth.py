#!/usr/bin/env python3
"""
Module of authentication views
"""
from flask import request
from typing import List, TypeVar


User = TypeVar('User')


class Auth:
    """ Authentication handler class """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Method to mark paths that require authentication """
        return False

    def authorization_header(self, request=None) -> str:
        """ Method to check the authorization header """
        return None

    def current_user(self, request=None) -> User:
        """ Method to check the current user """
        return None
