# Authors of the project:
# 1-MachnevEgor_https://vk.com/machnev_egor
# 2-DmitryShalimov_https://vk.com/lookatstat
# Contacts in email:
# 1-mea90608744@gmail.com
# 2-dmitriy-shalimov@yandex.ru

from discord.ext import commands
from BotConfig import *
from VariationPhrases import *
from random import randint

# variability of prefixes
client = commands.Bot(command_prefix=bot_prefixes)


# connection notification
@client.event
async def on_ready():
    print("Bot launched into the network")
    print("Name in network: {}".format(client.user))
    print("ID: {}".format(client.user.id))


# communication with the user
@client.event
async def on_message(message):
    msg = message.content.lower()
    if msg in ru_greetings_users:
        response_randomizer = randint(0, len(ru_greetings_bot) - 1)
        reply_to_greeting = ru_greetings_bot[response_randomizer]
        await message.channel.send(reply_to_greeting)
    if msg in eng_greetings_users:
        response_randomizer = randint(0, len(eng_greetings_bot) - 1)
        reply_to_greeting = eng_greetings_bot[response_randomizer]
        await message.channel.send(reply_to_greeting)


client.run(BotToken)

# Authors of the project:
# 1-MachnevEgor_https://vk.com/machnev_egor
# 2-DmitryShalimov_https://vk.com/lookatstat
# Contacts in email:
# 1-mea90608744@gmail.com
# 2-dmitriy-shalimov@yandex.ru
