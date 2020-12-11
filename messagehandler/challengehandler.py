import discord

from session.session import Session

class ChallengeHandler():
    @staticmethod
    async def handle_message(message: discord.Message, session_stage: int):
        await message.channel.send('Hello')