# Authors of the projects:
# 1-MachnevEgor_https://vk.com/machnev_egor
# 2-DmitryShalimov_https://vk.com/lookatstat
# Contacts in email:
# 1-mea90608744@gmail.com
# 2-dmitriy-shalimov@yandex.ru

def analysis_of_a_message_for_prefixes(msg, bot_prefixes):
    global collected_left_part_of_message, collected_right_part_of_message
    # creating a character-by-character array from a message
    check_for_prefixes = []
    for i in msg:
        check_for_prefixes.append(i)
    # creating a loop to iterate over and find all prefixes in the message
    len_bot_prefixes = len(bot_prefixes)
    prefix_check = 0
    while len_bot_prefixes != 0:
        prefix_from_prefixes = []
        for (i) in bot_prefixes[prefix_check]:
            prefix_from_prefixes.append(i)
        # analysis of the text for the presence of prefixes in the mention
        correct_quantity_checks = 0
        prefix_found = bool(False)
        quantity_checks = 0
        while quantity_checks != len(check_for_prefixes):
            if check_for_prefixes[quantity_checks] == prefix_from_prefixes[correct_quantity_checks]:
                correct_quantity_checks += 1
                if correct_quantity_checks == len(prefix_from_prefixes):
                    prefix_found = True
                    break
            else:
                correct_quantity_checks = 0
            quantity_checks += 1
        # creating two parts from a message
        if prefix_found == True:
            len_bot_prefixes = 0
            # left part of message without prefix
            left_part_of_message = []
            counter_of_processed_characters = 0
            while counter_of_processed_characters != (quantity_checks - len(prefix_from_prefixes) + 1):
                left_part_of_message.append(check_for_prefixes[counter_of_processed_characters])
                counter_of_processed_characters += 1
            collected_left_part_of_message = (''.join(left_part_of_message))
            # right part of message without prefix
            right_part_of_message = []
            counter_of_processed_characters = 0
            while counter_of_processed_characters != (len(check_for_prefixes) - quantity_checks - 1):
                right_part_of_message.append(check_for_prefixes[counter_of_processed_characters + quantity_checks + 1])
                counter_of_processed_characters += 1
            collected_right_part_of_message = (''.join(right_part_of_message))
        # repeat the operation if one of the prefixes did not match
        else:
            collected_left_part_of_message = "$N/O_N\E-T/E_X\T$"
            collected_right_part_of_message = "$N/O_N\E-T/E_X\T$"
            len_bot_prefixes -= 1
            prefix_check += 1

# import MessageAnalysis
# MessageAnalysis.analysis_of_a_message_for_prefixes(msg, bot_prefixes)
# left_part_of_message = MessageAnalysis.collected_left_part_of_message
# right_part_of_message = MessageAnalysis.collected_right_part_of_message

# bot_prefixes = ["owl", "сова"]
# msg = str.lower(input("-->"))
# analysis_of_a_message_for_prefixes(msg, bot_prefixes)
# if (collected_left_part_of_message != "$N/O_N\E-T/E_X\T$") and (collected_right_part_of_message != "$N/O_N\E-T/E_X\T$"):
#     print("Left part - ", collected_left_part_of_message)
#     print("Right part - ", collected_right_part_of_message)

# Authors of the projects:
# 1-MachnevEgor_https://vk.com/machnev_egor
# 2-DmitryShalimov_https://vk.com/lookatstat
# Contacts in email:
# 1-mea90608744@gmail.com
# 2-dmitriy-shalimov@yandex.ru
