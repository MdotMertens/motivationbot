import discord

from abc import ABC, abstractmethod
from session.sessionregistry import SessionRegistry
class Handler(ABC):

    @abstractmethod
    def set_next(self, handler):
        pass

    @abstractmethod
    def handle(self, message, session=None):
        pass


class AbstractHandler(Handler):
    _next_handler: Handler = None
    session_registry: SessionRegistry = SessionRegistry()

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, message, session=None):
        if self._next_handler:
            return self._next_handler.handle(message, session)

        return None


class MessageHandler(AbstractHandler):
    prefix = "!"

    def __init__(self):
        from .challengehandler import ChallengeHandler
        challenge_handler = ChallengeHandler()
        self.set_next(challenge_handler)

    async def handle(self, message: discord.Message, session=None):
        if session := super().session_registry.get_session(message.author):
            await super().handle(message, session)
        if message.content == self.prefix + 'challenge':
            session = super().session_registry.add_session(message.author, 'challenge')
            await super().handle(message, session)
