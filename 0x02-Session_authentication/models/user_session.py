#!/usr/bin/env python3
"""Module for saving user session information to a file"""

from models.base import Base


class UserSession(Base):
    """UserSession class"""
    def __init__(self, *args: list, **kwargs: dict):
        """ Constructor """
        self.user_id = kwargs.get('user_id')
        self.session_id = kwargs.get('session_id')
        super().__init__(*args, **kwargs)
