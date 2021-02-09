import warnings

import discord

from session.session import Session


class SessionRegistry(object):
    _registry = {}

    def add_session(self, user: discord.User, context=None):
        if self._registry.get(user, None) is None:
            session = Session(stage=0)
            if context is not None:
                session.context = context
            self._registry[user] = session
            return session
        else: warnings.warn("Session is already in progress.")

    def get_session(self, user: discord.User):
        return self._registry.get(user, None)

    def remove_session(self, user: discord.User):
        del self._registry[user]
    
    def update_session(self, user: discord.User, session: Session):
        if self._registry.get(user, None) is not None:
            self._registry[user] = session
