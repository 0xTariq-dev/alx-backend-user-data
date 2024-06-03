#!/usr/bin/env python3
"""
Module of authentication views
"""
from flask import request, abort
from typing import List, TypeVar


User = TypeVar('User')


class Auth:
    """ Authentication handler class """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Method to mark paths that require authentication """
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True
        if path[-1] != '/':
            path += '/'
        return path not in excluded_paths

    def authorization_header(self, request=None) -> str:
        """ Method to check the authorization header """
        if request is None or 'Authorization' not in request.headers:
            return None
        return request.headers['Authorization']

    def current_user(self, request=None) -> User:
        """ Method to check the current user """
        return None
