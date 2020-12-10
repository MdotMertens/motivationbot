import os
from dotenv import load_dotenv
load_dotenv()

import discord

from messagehandler.messagehandler import MessageHandler

client = discord.Client()
message_handler = MessageHandler()

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    else:
        await message_handler.handle_message(message)

client.run(os.getenv("DISCORD_TOKEN"))
