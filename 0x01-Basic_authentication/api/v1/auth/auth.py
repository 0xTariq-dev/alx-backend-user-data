#!/usr/bin/env python3
"""
Module of authentication views
"""
from flask import request, abort
from typing import List, TypeVar
import re


User = TypeVar('User')


class Auth:
    """ Authentication handler class """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Method to mark paths that require authentication """
        if path is not None and excluded_paths is not None:
            for p in excluded_paths:
                pattern = ''
                if p[-1] == '*':
                    pattern = rf'{p[:-1]}.*'
                elif p[-1] == '/':
                    pattern = rf'{p[:-1]}/*'
                else:
                    pattern = rf'{p}/*'
                if re.match(pattern, path):
                    return False
        return True

    def authorization_header(self, request=None) -> str:
        """ Method to check the authorization header """
        if request is None or 'Authorization' not in request.headers:
            return None
        return request.headers['Authorization']

    def current_user(self, request=None) -> User:
        """ Method to check the current user """
        return None
