import warnings

import discord

from session.session import Session


class SessionRegistry(object):
    _registry = {}

    def add_session(self, user: discord.User):
        if self._registry.get(user, None) is None:
            self._registry[user] = Session()
        else: warnings.warn("Session is already in progress.")

    def get_session(self, user: discord.User):
        return self._registry.get(user, None)

    def remove_session(self, user: discord.User):
        del self._registry[user]
