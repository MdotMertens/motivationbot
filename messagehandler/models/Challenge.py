import discord

class Challenge(object):

    def __init__(self, name: str, creator: discord.User):
        self.name = name
        self.creator = creator
        self.participants = []

    def add_participant(self, participant: discord.User):
        self.participants.append(participant)