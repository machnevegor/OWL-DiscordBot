# Authors of the project:
# 1-MachnevEgor_https://vk.com/machnev_egor
# 2-DmitryShalimov_https://vk.com/lookatstat
# Contacts in email:
# 1-mea90608744@gmail.com
# 2-dmitriy-shalimov@yandex.ru

import discord
from discord.ext import commands
from random import randint
import datetime
import BotConfig
import VariationPhrases
import MessageAnalysis
import BotAgeCalculation

client = discord.Client()

# variability of prefixes
client = commands.Bot(command_prefix=VariationPhrases.bot_prefixes)


# connection notification
@client.event
async def on_ready():
    # connection information
    print("-----------------------------")
    print("Bot launched into the network")
    print("Name in network: {}".format(client.user))
    print("ID: {}".format(client.user.id))
    print("-----------------------------")
    # a list of all participants who use the bot while connecting to the network
    for guild in client.guilds:
        if guild.name == client.user.id:
            break
    members = '\n - '.join([member.name for member in guild.members])
    print(f'All the friends of the bot:\n - {members}')
    print("-----------------------------")


# communication with the user
@client.event
async def on_message(message):
    # protection for checking the message of the bot itself
    if message.author == client.user:
        return

    # message processing and decomposition into commands
    input_msg = str(message.content)
    MessageAnalysis.start_message_analysis(input_msg)

    # inbound data on demand
    if MessageAnalysis.addressing_the_bot == True:
        print(datetime.datetime.today())
        print(message.author, "-->", message.content, sep="")
        print("Commands:", MessageAnalysis.msg_commands)

    # create a reply message
    message_from_bot = []

    # empty message
    # -->russian version
    if (MessageAnalysis.msg_commands == []) and (MessageAnalysis.addressing_the_bot == True) and (
            MessageAnalysis.prefix_number < len(VariationPhrases.ru_bot_prefixes)):
        response_randomizer = randint(0, len(VariationPhrases.ru_empty_message_bot) - 1)
        part_output_message = VariationPhrases.ru_empty_message_bot[response_randomizer]
        message_from_bot.append(part_output_message)
    # -->english version
    if (MessageAnalysis.msg_commands == []) and (MessageAnalysis.addressing_the_bot == True) and (
            MessageAnalysis.prefix_number >= len(VariationPhrases.ru_bot_prefixes)):
        response_randomizer = randint(0, len(VariationPhrases.eng_empty_message_bot) - 1)
        part_output_message = VariationPhrases.eng_empty_message_bot[response_randomizer]
        message_from_bot.append(part_output_message)

    # greetings
    # -->russian version
    quantity_checks = 0
    while (quantity_checks != len(MessageAnalysis.msg_commands)) and (MessageAnalysis.addressing_the_bot == True):
        if MessageAnalysis.msg_commands[quantity_checks] in VariationPhrases.ru_greetings_users:
            response_randomizer = randint(0, len(VariationPhrases.ru_greetings_bot) - 1)
            part_output_message = VariationPhrases.ru_greetings_bot[response_randomizer]
            message_from_bot.append(part_output_message)
            break
        quantity_checks += 1
    # -->english version
    quantity_checks = 0
    while (quantity_checks != len(MessageAnalysis.msg_commands)) and (MessageAnalysis.addressing_the_bot == True):
        if MessageAnalysis.msg_commands[quantity_checks] in VariationPhrases.eng_greetings_users:
            response_randomizer = randint(0, len(VariationPhrases.eng_greetings_bot) - 1)
            part_output_message = VariationPhrases.eng_greetings_bot[response_randomizer]
            message_from_bot.append(part_output_message)
            break
        quantity_checks += 1

    # what is the name of the owl
    # -->russian version
    quantity_checks = 0
    while (quantity_checks != len(MessageAnalysis.msg_commands)) and (MessageAnalysis.addressing_the_bot == True):
        if MessageAnalysis.msg_commands[quantity_checks] in VariationPhrases.ru_name_of_owl_users:
            response_randomizer = randint(0, len(VariationPhrases.ru_name_of_owl_bot) - 1)
            part_output_message = VariationPhrases.ru_name_of_owl_bot[response_randomizer]
            message_from_bot.append(part_output_message)
            break
        quantity_checks += 1
    # -->english version
    quantity_checks = 0
    while (quantity_checks != len(MessageAnalysis.msg_commands)) and (MessageAnalysis.addressing_the_bot == True):
        if MessageAnalysis.msg_commands[quantity_checks] in VariationPhrases.eng_name_of_owl_users:
            response_randomizer = randint(0, len(VariationPhrases.eng_name_of_owl_bot) - 1)
            part_output_message = VariationPhrases.eng_name_of_owl_bot[response_randomizer]
            message_from_bot.append(part_output_message)
            break
        quantity_checks += 1

    # who is an owl
    # -->russian version
    quantity_checks = 0
    while (quantity_checks != len(MessageAnalysis.msg_commands)) and (MessageAnalysis.addressing_the_bot == True):
        if MessageAnalysis.msg_commands[quantity_checks] in VariationPhrases.ru_who_is_an_owl_users:
            response_randomizer = randint(0, len(VariationPhrases.ru_who_is_an_owl_bot) - 1)
            part_output_message = VariationPhrases.ru_who_is_an_owl_bot[response_randomizer]
            message_from_bot.append(part_output_message)
            break
        quantity_checks += 1
    # -->english version
    quantity_checks = 0
    while (quantity_checks != len(MessageAnalysis.msg_commands)) and (MessageAnalysis.addressing_the_bot == True):
        if MessageAnalysis.msg_commands[quantity_checks] in VariationPhrases.eng_who_is_an_owl_users:
            response_randomizer = randint(0, len(VariationPhrases.eng_who_is_an_owl_bot) - 1)
            part_output_message = VariationPhrases.eng_who_is_an_owl_bot[response_randomizer]
            message_from_bot.append(part_output_message)
            break
        quantity_checks += 1

    # how old is the bot
    # -->russian version
    quantity_checks = 0
    while (quantity_checks != len(MessageAnalysis.msg_commands)) and (MessageAnalysis.addressing_the_bot == True):
        if MessageAnalysis.msg_commands[quantity_checks] in VariationPhrases.ru_how_old_is_the_bot:
            BotAgeCalculation.ru_years_old()
            if BotAgeCalculation.ru_bot_age != []:
                message_from_bot.append(BotAgeCalculation.ru_bot_age)
            break
        quantity_checks += 1
    # -->english version
    quantity_checks = 0
    while (quantity_checks != len(MessageAnalysis.msg_commands)) and (MessageAnalysis.addressing_the_bot == True):
        if MessageAnalysis.msg_commands[quantity_checks] in VariationPhrases.eng_how_old_is_the_bot:
            BotAgeCalculation.eng_years_old()
            if BotAgeCalculation.eng_bot_age != []:
                message_from_bot.append(BotAgeCalculation.eng_bot_age)
            break
        quantity_checks += 1

    # how are you
    # -->russian version
    quantity_checks = 0
    while (quantity_checks != len(MessageAnalysis.msg_commands)) and (MessageAnalysis.addressing_the_bot == True):
        if MessageAnalysis.msg_commands[quantity_checks] in VariationPhrases.ru_how_are_you_users:
            response_randomizer = randint(0, len(VariationPhrases.ru_how_are_you_bot) - 1)
            part_output_message = VariationPhrases.ru_how_are_you_bot[response_randomizer]
            message_from_bot.append(part_output_message)
            break
        quantity_checks += 1
    # -->english version
    quantity_checks = 0
    while (quantity_checks != len(MessageAnalysis.msg_commands)) and (MessageAnalysis.addressing_the_bot == True):
        if MessageAnalysis.msg_commands[quantity_checks] in VariationPhrases.eng_how_are_you_users:
            response_randomizer = randint(0, len(VariationPhrases.eng_how_are_you_bot) - 1)
            part_output_message = VariationPhrases.eng_how_are_you_bot[response_randomizer]
            message_from_bot.append(part_output_message)
            break
        quantity_checks += 1

    # what are you doing
    # -->russian version
    quantity_checks = 0
    while (quantity_checks != len(MessageAnalysis.msg_commands)) and (MessageAnalysis.addressing_the_bot == True):
        if MessageAnalysis.msg_commands[quantity_checks] in VariationPhrases.ru_what_are_you_doing_users:
            response_randomizer = randint(0, len(VariationPhrases.ru_what_are_you_doing_bot) - 1)
            part_output_message = VariationPhrases.ru_what_are_you_doing_bot[response_randomizer]
            message_from_bot.append(part_output_message)
            break
        quantity_checks += 1
    # -->english version
    quantity_checks = 0
    while (quantity_checks != len(MessageAnalysis.msg_commands)) and (MessageAnalysis.addressing_the_bot == True):
        if MessageAnalysis.msg_commands[quantity_checks] in VariationPhrases.eng_what_are_you_doing_users:
            response_randomizer = randint(0, len(VariationPhrases.eng_what_are_you_doing_bot) - 1)
            part_output_message = VariationPhrases.eng_what_are_you_doing_bot[response_randomizer]
            message_from_bot.append(part_output_message)
            break
        quantity_checks += 1

    # heads or tails
    # -->russian version
    quantity_checks = 0
    while (quantity_checks != len(MessageAnalysis.msg_commands)) and (MessageAnalysis.addressing_the_bot == True):
        if MessageAnalysis.msg_commands[quantity_checks] in VariationPhrases.ru_heads_or_tails_users:
            part_output_message = []
            response_randomizer = randint(0, len(VariationPhrases.ru_heads_or_tails_bot) - 1)
            part_output_message.append(VariationPhrases.ru_heads_or_tails_bot[response_randomizer])
            heads_or_tails_randomizer = randint(0, 1)
            if heads_or_tails_randomizer == 0:
                part_output_message.append("Орёл)")
            else:
                part_output_message.append("Решка)")
            message_from_bot.append(' '.join(part_output_message))
        quantity_checks += 1
    # -->english version
    quantity_checks = 0
    while (quantity_checks != len(MessageAnalysis.msg_commands)) and (MessageAnalysis.addressing_the_bot == True):
        if MessageAnalysis.msg_commands[quantity_checks] in VariationPhrases.eng_heads_or_tails_users:
            part_output_message = []
            response_randomizer = randint(0, len(VariationPhrases.eng_heads_or_tails_bot) - 1)
            part_output_message.append(VariationPhrases.eng_heads_or_tails_bot[response_randomizer])
            heads_or_tails_randomizer = randint(0, 1)
            if heads_or_tails_randomizer == 0:
                part_output_message.append("Head)")
            else:
                part_output_message.append("Tail)")
            message_from_bot.append(' '.join(part_output_message))
        quantity_checks += 1

    # messages with delusions
    if (message_from_bot == []) and (MessageAnalysis.addressing_the_bot == True):
        # -->russian version
        if MessageAnalysis.prefix_number < len(VariationPhrases.ru_bot_prefixes):
            response_randomizer = randint(0, len(VariationPhrases.ru_messages_with_delusions_bot) - 1)
            part_output_message = VariationPhrases.ru_messages_with_delusions_bot[response_randomizer]
            message_from_bot.append(part_output_message)
        # -->english version
        else:
            response_randomizer = randint(0, len(VariationPhrases.eng_messages_with_delusions_bot) - 1)
            part_output_message = VariationPhrases.eng_messages_with_delusions_bot[response_randomizer]
            message_from_bot.append(part_output_message)

    # sending a summary message
    if message_from_bot != []:
        await message.channel.send(' '.join(message_from_bot))
        print("Response:", " ".join(message_from_bot))
        print("-----------------------------")


client.run(BotConfig.BotToken)

# Authors of the project:
# 1-MachnevEgor_https://vk.com/machnev_egor
# 2-DmitryShalimov_https://vk.com/lookatstat
# Contacts in email:
# 1-mea90608744@gmail.com
# 2-dmitriy-shalimov@yandex.ru
