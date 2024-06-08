#!/usr/bin/env python3
"""Module for saving session authenticantion token to a file"""

from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession


class SessionDBAuth(SessionExpAuth):
    """SessionDBAuth class"""
    def create_session(self, user_id=None):
        """ Create a session for the user_id """
        session_id = super().create_session(user_id)
        if session_id is None:
            return None
        session = UserSession(user_id=user_id, session_id=session_id)
        session.save()
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """ Return the user_id by requesting it from the UserSession """
        if session_id is None:
            return None
        try:
            users = UserSession.search({'session_id': session_id})
        except Exception:
            return None
        if not users:
            return None
        user = users[0]
        if super().user_id_for_session_id(session_id) != user.user_id:
            return None
        return user.user_id

    def destroy_session(self, request=None):
        """ Destroy a session by deleting it from the database """
        if request is None:
            return False
        session_id = self.session_cookie(request)
        if session_id is None:
            return False
        try:
            users = UserSession.search({'session_id': session_id})
        except Exception:
            return False
        if not users:
            return False
        user = users[0]
        user.remove()
        return True
