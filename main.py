import os
from dotenv import load_dotenv
load_dotenv()
import discord
client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.autho == client.user:
        return
    
    if message.content.startswith('!test'):
        await message.channel.send('Passed!')

client.run(os.getenv("DISCORD_TOKEN"))