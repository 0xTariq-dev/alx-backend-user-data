#!/usr/bin/env python3
""" Module for session authentication with expiration date """

from os import getenv
from datetime import datetime, timedelta
from api.v1.auth.session_auth import SessionAuth


class SessionExpAuth(SessionAuth):
    """ SessionExpAuth class
    """
    def __init__(self):
        """ Constructor """
        self.session_duration = int(getenv('SESSION_DURATION', 0))
        super().__init__()

    def create_session(self, user_id=None):
        """ Create a session for the user_id """
        session_id = super().create_session(user_id)
        if session_id is None:
            return None
        session_dictionary = {
            "user_id": user_id,
            "created_at": datetime.now()
        }
        self.user_id_by_session_id[session_id] = session_dictionary
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """ Return a User ID based on a Session ID """
        if session_id is None:
            return None
        session_dictionary = self.user_id_by_session_id.get(session_id)
        if session_dictionary is None:
            return None
        if self.session_duration <= 0:
            return session_dictionary.get('user_id')
        if 'created_at' not in session_dictionary:
            return None
        created_at = session_dictionary.get('created_at')
        if created_at is None:
            return None
        expiration_date = created_at + timedelta(seconds=self.session_duration)
        if expiration_date < datetime.now():
            return None
        return session_dictionary.get('user_id')
