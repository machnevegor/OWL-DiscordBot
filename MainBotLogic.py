import discord
from discord.ext import commands
from BotConfig import *
from ServerSettings import *

# variability of prefixes
client = commands.Bot(
    command_prefix=["owl ", "Owl ", "OWL ", "owl, ", "Owl, ", "OWL, ", "сова ", "Сова ", "СОВА ", "сова, ", "Сова, ",
                    "СОВА, "])


# connection notification
@client.event
async def on_ready():
    print("Bot launched into the network")
    print("Name: {}".format(client.user))
    print("ID: {}".format(client.user.id))


# greetings
@client.command(pass_context=True)
async def hello(ctx):
    await ctx.send('Hello!')


client.run(BotToken)
