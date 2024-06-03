#!/usr/bin/env python3
"""
Module of authentication views
"""
from api.v1.auth.auth import Auth


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
