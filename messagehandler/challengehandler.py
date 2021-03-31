import discord

from datetime import datetime, date

from messagehandler.handler import AbstractHandler
from session.session import Session
from .models.Challenge import Challenge


class ChallengeHandler(AbstractHandler):
    async def handle(self, message: discord.Message, session: Session):
        if message.content: 
            if session.stage == 0:
                response = "What do you wnat your Challenge to be called?"
                await message.channel.send(response)
                session.stage += 1
            elif session.stage == 1:
                session.challenge = Challenge(message.content,message.author)
                await message.channel.send("Created challenge with name {}".format(session.challenge.name))
                await message.channel.send("When do you want this challenge to start? (Format: DD/MM/YYYY)")
                session.stage += 1
                await message.channel.send("When do you want your challenge to start? (Format: DD/MM/YYYY)")
            elif session.stage == 2:
                if date := self.date_from_message(message.content):
                    if self.check_if_date_is_valid(date):
                        session.challenge.start_date = date
                        await message.channel.send("Set the start date of challenge {} to {}".format(session.challenge.name,session.challenge.start_date))
                        session.stage += 1
                        await message.channel.send("When do you want to end your challenge? (Fromat: DD/MM/YYYY)")
                    else: 
                        await message.channel.send("Cannot set date. Date is in the past.")
                else:
                    await message.channel.send("Failed to set date.")

            elif session.stage == 3:
                if date := self.date_from_message(message.content):
                    if session.challenge.start_date > date:
                        await message.channel.send("End date cannot be before start date!")
                    else:
                         session.challenge.end_date = date
                         await message.channel.send("Set the end date of challenge {} to {}".format(session.challenge.name,session.challenge.end_date))
                         session.stage += 1
                         await message.channel.send("Who do you want to invite to your challenge? Add them with a mention.")
                else:
                    await message.channel.send("Failed to set date")

            elif session.stage == 4:
                for mention in message.mentions:
                    session.challenge.add_participant(mention)
                session.stage += 1
                await message.channel.send(' '.join(map(str, session.challenge.participants)))

    def date_from_message(self, date_string):
        split_string = date_string.split("/", 3)
        try:
            return date(int(split_string[2]), int(split_string[1]), int(split_string[0]))
        except ValueError:
            return None

    def check_if_date_is_valid(self, date: date):
        if date < datetime.now().date():
            return False
        return True
