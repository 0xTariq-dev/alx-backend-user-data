#!/usr/bin/env python3
"""
Module of authentication views
"""
from api.v1.auth.auth import Auth
from base64 import b64decode
from typing import Tuple, TypeVar
from models.user import User


class BasicAuth(Auth):
    """ Basic authentication handler class """
    def extract_base64_authorization_header(self,
                                            authorization_header: str
                                            ) -> str:
        """ Method to extract the base64 part of the Authorization header """
        if not authorization_header or type(authorization_header) is not str:
            return None
        if not authorization_header.startswith('Basic '):
            return None
        return authorization_header.strip('Basic ')

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> str:
        """ Method to decode a base64 string """
        if not base64_authorization_header or \
                type(base64_authorization_header) is not str:
            return None
        try:
            return b64decode(base64_authorization_header).decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str
                                 ) -> Tuple[str, str]:
        """ Method to extract user credentials """
        if not decoded_base64_authorization_header or \
                type(decoded_base64_authorization_header) is not str or \
                ':' not in decoded_base64_authorization_header:
            return (None, None)
        return tuple(decoded_base64_authorization_header.split(':', 1))

    def user_object_from_credentials(self,
                                     user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """ Method to get a user object from credentials """
        if type(user_email) == str and type(user_pwd) == str:
            try:
                users = User.search({'email': user_email})
            except Exception:
                return None
            if len(users) <= 0:
                return None
            if users[0].is_valid_password(user_pwd):
                return users[0]
        return None
