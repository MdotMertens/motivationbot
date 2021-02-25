import discord

from messagehandler.handler import AbstractHandler
from session.session import Session
from .models.Challenge import Challenge


class ChallengeHandler(AbstractHandler):
    async def handle(self, message: discord.Message, session: Session):
        if session.stage == 0:
            await message.channel.send('What do you want your Challenge to be called?')
            session.stage += 1
        elif session.stage == 1:
            if message.content:
                session.challenge = Challenge(message.content,message.author)
                await message.channel.send("Created challenge with name {}".format(session.challenge.name))
                await message.channel.send("When do you want this challenge to start? (Format: DD/MM/YYYY)")
                session.stage += 1
        elif session.stage == 2:
            if message.content:
                challenge = session.challenge
                for mention in message.mentions:
                    challenge.add_participant(mention)
