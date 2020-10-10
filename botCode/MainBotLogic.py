# Authors of the project:
# 1-MachnevEgor_https://vk.com/machnev_egor
# 2-DmitryShalimov_https://vk.com/lookatstat
# Contacts in email:
# 1-meb.official.com@gmail.com
# 2-dmitriy-shalimov@yandex.ru

########################################################################################################################

# IMPORT MAIN LIBRARIES
import discord as discord
from discord import Activity, ActivityType
from discord.ext import commands as commands
from configurationFile import BotConfig as BotConfig
from asyncio import sleep as asyncio_sleep
import datetime as datetime
from analysisCode import MessageAnalysis as MessageAnalysis
from threading import Thread as Thread
from analysisCode import ConformityAnalysis as ConformityAnalysis
from random import randint as randint
from phrasesDatabase import VariationPhrases as VariationPhrases
from featuresCode import BotAgeCalculation as BotAgeCalculation

########################################################################################################################

# CREATE DISCORD CLIENT AND THE LIKE
# create discord client
client = discord.Client()
# variability of prefixes
client = commands.Bot(command_prefix=VariationPhrases.ctx_bot_prefixes)


########################################################################################################################

# SENDING DATA IN TERMINAL ON STARTUP
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
    members = "\n|♡|➳".join([guild.name for guild in client.guilds])
    print(f"|♡|All friends of the bot:\n|♡|➳ {members}")
    print("-----------------------------")
    # the status of the bot
    client.loop.create_task(status_task())
    
########################################################################################################################

# THE STATUS OF THE BOT
# asynchronous function that changes the bot status over time
async def status_task():
    while True:
        # generating a new status
        status_correspondence_randomizer = randint(0, 3)
        if status_correspondence_randomizer == 0:
            status_text_randomizer = randint(0, len(VariationPhrases.game_bot_status) - 1)
            status_text = VariationPhrases.game_bot_status[status_text_randomizer]
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=status_text))
        elif status_correspondence_randomizer == 1:
            status_text_randomizer = randint(0, len(VariationPhrases.watch_bot_status) - 1)
            status_text = VariationPhrases.watch_bot_status[status_text_randomizer]
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=status_text))
        elif status_correspondence_randomizer == 2:
            status_text_randomizer = randint(0, len(VariationPhrases.stream_bot_status) - 1)
            status_text = VariationPhrases.stream_bot_status[status_text_randomizer]
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.streaming, name=status_text))
        elif status_correspondence_randomizer == 3:
            status_text_randomizer = randint(0, len(VariationPhrases.listen_bot_status) - 1)
            status_text = VariationPhrases.listen_bot_status[status_text_randomizer]
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=status_text))
        # sending data in terminal
        print(datetime.datetime.today())
        print(f"New status: {status_text}")
        print("-----------------------------")
        # async sleep
        await asyncio_sleep(5 * 60)


########################################################################################################################

# COMMUNICATION OF THE BOT WITH THE USER
# chat between the bot and the user with a new message
@client.event
async def on_message(message):
    # protection for checking the message of the bot itself
    if message.author == client.user:
        return

    # message processing and decomposition into commands
    input_msg = str(message.content)
    MessageAnalysis.start_message_analysis(input_msg)

    ####################################################################################################################

    # SENDING DATA IN TERMINAL
    # inbound data on demand
    if MessageAnalysis.addressing_the_bot == True:
        print(datetime.datetime.today())
        print(message.guild.name, "-->", message.author, "-->", message.content, sep="")
        if MessageAnalysis.msg_commands != []:
            print("Commands:", MessageAnalysis.msg_commands)
        if MessageAnalysis.msg_links != []:
            print("Youtube-links:", ", ".join(MessageAnalysis.msg_links))

    ####################################################################################################################

    # MAIN OUTPUT VARIABLES
    # create a reply message
    message_from_bot = []
    # create array with requested embeds
    embed_from_bot = []

    ####################################################################################################################

    # EMPTY MESSAGE
    # empty message with a request
    # -->ctx version
    if (MessageAnalysis.msg_commands == []) and (MessageAnalysis.addressing_the_bot == True) and (
            MessageAnalysis.prefix_number < len(VariationPhrases.ctx_bot_prefixes)):
        response_randomizer = randint(0, len(VariationPhrases.ctx_empty_message_bot) - 1)
        part_output_message = VariationPhrases.ctx_empty_message_bot[response_randomizer]
        message_from_bot.append(part_output_message)
    # -->russian version
    if (MessageAnalysis.msg_commands == []) and (MessageAnalysis.addressing_the_bot == True) and (
            (MessageAnalysis.prefix_number - len(VariationPhrases.ctx_bot_prefixes)) < len(
        VariationPhrases.ru_bot_prefixes)) and (
            MessageAnalysis.prefix_number >= len(VariationPhrases.ctx_bot_prefixes)):
        response_randomizer = randint(0, len(VariationPhrases.ru_empty_message_bot) - 1)
        part_output_message = VariationPhrases.ru_empty_message_bot[response_randomizer]
        message_from_bot.append(part_output_message)
    # -->english version
    if (MessageAnalysis.msg_commands == []) and (MessageAnalysis.addressing_the_bot == True) and (
            (MessageAnalysis.prefix_number - len(VariationPhrases.ctx_bot_prefixes)) >= len(
        VariationPhrases.ru_bot_prefixes)) and (
            MessageAnalysis.prefix_number >= len(VariationPhrases.ctx_bot_prefixes)):
        response_randomizer = randint(0, len(VariationPhrases.eng_empty_message_bot) - 1)
        part_output_message = VariationPhrases.eng_empty_message_bot[response_randomizer]
        message_from_bot.append(part_output_message)

    ####################################################################################################################

    # MAIN COMMUNICATION
    # if there was an appeal to the bot and communication is possible
    if (MessageAnalysis.msg_commands != []) and (MessageAnalysis.addressing_the_bot == True):

        # 1) GREETINGS
        # owl greeting with user
        def ru_and_eng_greetigs(quantity_commands_checks):
            # -->russian version
            if MessageAnalysis.msg_commands[quantity_commands_checks] in VariationPhrases.ru_greetings_users:
                response_randomizer = randint(0, len(VariationPhrases.ru_greetings_bot) - 1)
                part_output_message = VariationPhrases.ru_greetings_bot[response_randomizer]
                message_from_bot.append(part_output_message)
            # -->english version
            if MessageAnalysis.msg_commands[quantity_commands_checks] in VariationPhrases.eng_greetings_users:
                response_randomizer = randint(0, len(VariationPhrases.eng_greetings_bot) - 1)
                part_output_message = VariationPhrases.eng_greetings_bot[response_randomizer]
                message_from_bot.append(part_output_message)

        # GREETINGS - sequential command processing for a logical structured response
        for quantity_commands_checks in range(len(MessageAnalysis.msg_commands)):
            Thread(target=ru_and_eng_greetigs(quantity_commands_checks)).start()

        # 2) ACQUAINTANCE AND THE LIKE
        # what is the name of the owl
        def ru_and_eng_what_is_the_name_of_the_owl(quantity_commands_checks):
            # -->russian version
            ConformityAnalysis.find_command_matches(msg_command=MessageAnalysis.msg_commands[quantity_commands_checks],
                                                    prepared_questions_matrix=VariationPhrases.ru_name_of_owl_users,
                                                    array_required_matches=[[0, 1, 2]])
            if ConformityAnalysis.presence_coincidence == True:
                response_randomizer = randint(0, len(VariationPhrases.ru_name_of_owl_bot) - 1)
                part_output_message = VariationPhrases.ru_name_of_owl_bot[response_randomizer]
                message_from_bot.append(part_output_message)
            # -->english version
            ConformityAnalysis.find_command_matches(msg_command=MessageAnalysis.msg_commands[quantity_commands_checks],
                                                    prepared_questions_matrix=VariationPhrases.eng_name_of_owl_users,
                                                    array_required_matches=[[0, 1, 2]])
            if ConformityAnalysis.presence_coincidence == True:
                response_randomizer = randint(0, len(VariationPhrases.eng_name_of_owl_bot) - 1)
                part_output_message = VariationPhrases.eng_name_of_owl_bot[response_randomizer]
                message_from_bot.append(part_output_message)

        # who is an owl
        def ru_and_eng_who_is_an_owl(quantity_commands_checks):
            # -->russian version
            if MessageAnalysis.msg_commands[quantity_commands_checks] in VariationPhrases.ru_who_is_an_owl_users:
                response_randomizer = randint(0, len(VariationPhrases.ru_who_is_an_owl_bot) - 1)
                part_output_message = VariationPhrases.ru_who_is_an_owl_bot[response_randomizer]
                message_from_bot.append(part_output_message)
            # -->english version
            if MessageAnalysis.msg_commands[quantity_commands_checks] in VariationPhrases.eng_who_is_an_owl_users:
                response_randomizer = randint(0, len(VariationPhrases.eng_who_is_an_owl_bot) - 1)
                part_output_message = VariationPhrases.eng_who_is_an_owl_bot[response_randomizer]
                message_from_bot.append(part_output_message)

        # how old is the bot
        def ru_and_eng_how_old_is_the_bot(quantity_commands_checks):
            # -->russian version
            ConformityAnalysis.find_command_matches(msg_command=MessageAnalysis.msg_commands[quantity_commands_checks],
                                                    prepared_questions_matrix=VariationPhrases.ru_how_old_is_the_bot,
                                                    array_required_matches=[[0, 1]])
            if ConformityAnalysis.presence_coincidence == True:
                BotAgeCalculation.ru_years_old()
                if BotAgeCalculation.ru_bot_age != []:
                    message_from_bot.append(BotAgeCalculation.ru_bot_age)
            # -->english version
            ConformityAnalysis.find_command_matches(msg_command=MessageAnalysis.msg_commands[quantity_commands_checks],
                                                    prepared_questions_matrix=VariationPhrases.eng_how_old_is_the_bot,
                                                    array_required_matches=[[0, 1]])
            if ConformityAnalysis.presence_coincidence == True:
                BotAgeCalculation.eng_years_old()
                if BotAgeCalculation.eng_bot_age != []:
                    message_from_bot.append(BotAgeCalculation.eng_bot_age)

        # ACQUAINTANCE AND THE LIKE - sequential command processing for a logical structured response
        for quantity_commands_checks in range(len(MessageAnalysis.msg_commands)):
            Thread(target=ru_and_eng_what_is_the_name_of_the_owl(quantity_commands_checks)).start()
            Thread(target=ru_and_eng_who_is_an_owl(quantity_commands_checks)).start()
            Thread(target=ru_and_eng_how_old_is_the_bot(quantity_commands_checks)).start()

        # 3) COMMUNICATION
        # how are you
        def ru_and_eng_how_are_you(quantity_commands_checks):
            # -->russian version
            ConformityAnalysis.find_command_matches(msg_command=MessageAnalysis.msg_commands[quantity_commands_checks],
                                                    prepared_questions_matrix=VariationPhrases.ru_how_are_you_users,
                                                    array_required_matches=[[0, 1]])
            if ConformityAnalysis.presence_coincidence == True:
                response_randomizer = randint(0, len(VariationPhrases.ru_how_are_you_bot) - 1)
                part_output_message = VariationPhrases.ru_how_are_you_bot[response_randomizer]
                message_from_bot.append(part_output_message)
            # -->english version
            if MessageAnalysis.msg_commands[quantity_commands_checks] in VariationPhrases.eng_how_are_you_users:
                response_randomizer = randint(0, len(VariationPhrases.eng_how_are_you_bot) - 1)
                part_output_message = VariationPhrases.eng_how_are_you_bot[response_randomizer]
                message_from_bot.append(part_output_message)

        # what are you doing
        def ru_and_eng_what_are_you_doing(quantity_commands_checks):
            # -->russian version
            ConformityAnalysis.find_command_matches(msg_command=MessageAnalysis.msg_commands[quantity_commands_checks],
                                                    prepared_questions_matrix=VariationPhrases.ru_what_are_you_doing_users,
                                                    array_required_matches=[[0, 1]])
            if ConformityAnalysis.presence_coincidence == True:
                response_randomizer = randint(0, len(VariationPhrases.ru_what_are_you_doing_bot) - 1)
                part_output_message = VariationPhrases.ru_what_are_you_doing_bot[response_randomizer]
                message_from_bot.append(part_output_message)
            # -->english version
            ConformityAnalysis.find_command_matches(msg_command=MessageAnalysis.msg_commands[quantity_commands_checks],
                                                    prepared_questions_matrix=VariationPhrases.eng_what_are_you_doing_users,
                                                    array_required_matches=[[0, 1]])
            if ConformityAnalysis.presence_coincidence == True:
                response_randomizer = randint(0, len(VariationPhrases.eng_what_are_you_doing_users) - 1)
                part_output_message = VariationPhrases.eng_what_are_you_doing_users[response_randomizer]
                message_from_bot.append(part_output_message)

        # COMMUNICATION - sequential command processing for a logical structured response
        for quantity_commands_checks in range(len(MessageAnalysis.msg_commands)):
            Thread(target=ru_and_eng_how_are_you(quantity_commands_checks)).start()
            Thread(target=ru_and_eng_what_are_you_doing(quantity_commands_checks)).start()

        # 4) FEATURES
        # heads or tails
        def ru_and_eng_heads_or_tails(quantity_commands_checks):
            # -->russian version 
            ConformityAnalysis.find_command_matches(msg_command=MessageAnalysis.msg_commands[quantity_commands_checks],
                                                    prepared_questions_matrix=VariationPhrases.ru_heads_or_tails_users,
                                                    array_required_matches=[[0, 1], [2, 3]])
            if ConformityAnalysis.presence_coincidence == True:
                part_output_message = []
                response_randomizer = randint(0, len(VariationPhrases.ru_heads_or_tails_bot) - 1)
                part_output_message.append(VariationPhrases.ru_heads_or_tails_bot[response_randomizer])
                heads_or_tails_randomizer = randint(0, 1)
                if heads_or_tails_randomizer == 0:
                    part_output_message.append("Орёл)")
                else:
                    part_output_message.append("Решка)")
                message_from_bot.append(" ".join(part_output_message))
            # -->english version
            ConformityAnalysis.find_command_matches(msg_command=MessageAnalysis.msg_commands[quantity_commands_checks],
                                                    prepared_questions_matrix=VariationPhrases.eng_heads_or_tails_users,
                                                    array_required_matches=[[0, 1], [2, 3]])
            if ConformityAnalysis.presence_coincidence == True:
                part_output_message = []
                response_randomizer = randint(0, len(VariationPhrases.eng_heads_or_tails_bot) - 1)
                part_output_message.append(VariationPhrases.eng_heads_or_tails_bot[response_randomizer])
                heads_or_tails_randomizer = randint(0, 1)
                if heads_or_tails_randomizer == 0:
                    part_output_message.append("Head)")
                else:
                    part_output_message.append("Tail)")
                message_from_bot.append(" ".join(part_output_message))

        # FEATURES - sequential command processing for a logical structured response
        for quantity_commands_checks in range(len(MessageAnalysis.msg_commands)):
            Thread(target=ru_and_eng_heads_or_tails(quantity_commands_checks)).start()

        # 5) EMBEDS
        # embed - who are your developers
        def ru_and_eng_who_are_your_developers(quantity_commands_checks, embed_from_bot):
            # -->russian version
            ConformityAnalysis.find_command_matches(msg_command=MessageAnalysis.msg_commands[quantity_commands_checks],
                                                    prepared_questions_matrix=VariationPhrases.ru_who_are_your_developers_users,
                                                    array_required_matches=[[0, 1], [2, 3]])
            if ConformityAnalysis.presence_coincidence == True:
                response_randomizer = randint(0, len(VariationPhrases.ru_who_are_your_developers_bot) - 1)
                part_output_message = VariationPhrases.ru_who_are_your_developers_bot[response_randomizer]
                message_from_bot.append(part_output_message)
                embed_from_bot.append("ru_developers_availability_emb")
            # -->english version
            ConformityAnalysis.find_command_matches(msg_command=MessageAnalysis.msg_commands[quantity_commands_checks],
                                                    prepared_questions_matrix=VariationPhrases.eng_who_are_your_developers_users,
                                                    array_required_matches=[[0, 1, 2], [0, 3]])
            if ConformityAnalysis.presence_coincidence == True:
                response_randomizer = randint(0, len(VariationPhrases.eng_who_are_your_developers_bot) - 1)
                part_output_message = VariationPhrases.eng_who_are_your_developers_bot[response_randomizer]
                message_from_bot.append(part_output_message)
                embed_from_bot.append("eng_developers_availability_emb")

        # EMBEDS - sequential command processing for a logical structured response
        for quantity_commands_checks in range(len(MessageAnalysis.msg_commands)):
            Thread(target=ru_and_eng_who_are_your_developers(quantity_commands_checks, embed_from_bot)).start()

    ####################################################################################################################

    # MESSAGE WITH DELUSIONS
    # if the bot did not recognize the message and cannot reply
    if (message_from_bot == []) and (MessageAnalysis.addressing_the_bot == True) and (embed_from_bot == []):
        # -->ctx version
        if MessageAnalysis.prefix_number < len(VariationPhrases.ctx_bot_prefixes):
            response_randomizer = randint(0, len(VariationPhrases.ctx_messages_with_delusions_bot) - 1)
            part_output_message = VariationPhrases.ctx_messages_with_delusions_bot[response_randomizer]
            message_from_bot.append(part_output_message)
        # -->russian version
        if ((MessageAnalysis.prefix_number - len(VariationPhrases.ctx_bot_prefixes)) < len(
                VariationPhrases.ru_bot_prefixes)) and (
                MessageAnalysis.prefix_number >= len(VariationPhrases.ctx_bot_prefixes)):
            response_randomizer = randint(0, len(VariationPhrases.ru_messages_with_delusions_bot) - 1)
            part_output_message = VariationPhrases.ru_messages_with_delusions_bot[response_randomizer]
            message_from_bot.append(part_output_message)
        # -->english version
        if ((MessageAnalysis.prefix_number - len(VariationPhrases.ctx_bot_prefixes)) >= len(
                VariationPhrases.ru_bot_prefixes)) and (
                MessageAnalysis.prefix_number >= len(VariationPhrases.ctx_bot_prefixes)):
            response_randomizer = randint(0, len(VariationPhrases.eng_messages_with_delusions_bot) - 1)
            part_output_message = VariationPhrases.eng_messages_with_delusions_bot[response_randomizer]
            message_from_bot.append(part_output_message)

    ####################################################################################################################

    # SENDING A RESPONCE
    # sending a summary message
    if message_from_bot != []:
        await message.channel.send(" ".join(message_from_bot))

    # sending embeds
    if ("ru_developers_availability_emb" in embed_from_bot):
        ru_developers_emb = discord.Embed(title="OWL-ДискордБот", colour=discord.Color.blue(),
                                          url=BotConfig.link_to_bot_site)
        ru_developers_emb.add_field(name="Проектное сообщество:", value="SM_TECHNOLOGY", inline=True)
        ru_developers_emb.add_field(name="Разработчики:", value="Мачнев Егор\nДмитрий Шалимов", inline=True)
        await message.channel.send(embed=ru_developers_emb)
    if ("eng_developers_availability_emb" in embed_from_bot):
        eng_developers_emb = discord.Embed(title="OWL-DiscordBot", colour=discord.Color.blue(),
                                           url=BotConfig.link_to_bot_site)
        eng_developers_emb.add_field(name="Project community:", value="SM_TECHNOLOGY", inline=True)
        eng_developers_emb.add_field(name="Developers:", value="Machnev Egor\nDmitriy Schalimov", inline=True)
        await message.channel.send(embed=eng_developers_emb)

    ####################################################################################################################

    # SENDING DATA IN TERMINAL
    # sending data to the terminal about the final message
    if message_from_bot != []:
        print("Response:", " ".join(message_from_bot))
        if embed_from_bot != []:
            print("Embeds:", ", ".join(embed_from_bot))
        print("-----------------------------")


########################################################################################################################

client.run(BotConfig.BotToken)

########################################################################################################################

# Authors of the project:
# 1-MachnevEgor_https://vk.com/machnev_egor
# 2-DmitryShalimov_https://vk.com/lookatstat
# Contacts in email:
# 1-meb.official.com@gmail.com
# 2-dmitriy-shalimov@yandex.ru
