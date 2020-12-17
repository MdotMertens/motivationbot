import discord

from messagehandler.handler import AbstractHandler
from session.session import Session


class ChallengeHandler(AbstractHandler):
    async def handle(self, message: discord.Message, session: Session):
        if session.stage == 0:
            session.stage += 1
            super().session_registry._registry[message.author] = session
            await message.channel.send('What do you want your Challenge to be called?')
        elif session.stage == 1:
            session.stage += 1
            super().session_registry._registry[message.author] = session
            await message.channel.send('Hell Yeah!')