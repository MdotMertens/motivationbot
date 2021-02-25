import os
import discord
from messagehandler.handler import MessageHandler
from dotenv import load_dotenv
load_dotenv()

client = discord.Client()
message_handler = MessageHandler()


@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))


@client.event
async def on_message(message: discord.Message):
    if message.author == client.user:
        return
    else:
        await message_handler.handle(message)

client.run(os.getenv("DISCORD_TOKEN"))
