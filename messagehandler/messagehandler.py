import discord
from session.sessionregistry import SessionRegistry
from challengehandler import ChallengeHandler

class MessageHandler(object):

    def __init__(self):
        self.session_registry = SessionRegistry()
        self.prefix = '!'
    # Handler is responsible for creating and managing sessions
    # The handler assigns a given keyword to an instance of a class which
    # then handles the message accordingly
    async def handle_message(self, message: discord.Message):
        session = self.session_registry.get_session(message.author)
        if session is None:
            self.session_registry.add_session(message.author)
            if message.content == self.prefix + 'challenge':
               session.set_context('challenge') 
               await  message.channel.send("Successfully created a challenge session!")

        else:
            if message.content == self.prefix + 'exit':
                self.session_registry.remove_session(message.author)
                await message.channel.send("Goodbye!")
            elif session.context == 'challenge':
                ChallengeHandler.handle_message(message,session.stage)

            else:
                await message.channel.send("We've got a Session!")
