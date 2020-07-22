# Authors of the projects:
# 1-MachnevEgor_https://vk.com/machnev_egor
# 2-DmitryShalimov_https://vk.com/lookatstat
# Contacts in email:
# 1-mea90608744@gmail.com
# 2-dmitriy-shalimov@yandex.ru

# removing unnecessary words that play the role of punctuation marks
def simplifying_texts_for_defining_basic_commands(memory_array):
    # creating a shared array
    unnecessary_words = []
    number_of_words_processed = 0
    while number_of_words_processed != len(bot_prefixes):
        unnecessary_words.append(bot_prefixes[number_of_words_processed])
        number_of_words_processed += 1
    number_of_words_processed = 0
    while number_of_words_processed != len(union_words):
        unnecessary_words.append(union_words[number_of_words_processed])
        number_of_words_processed += 1
    # going through all possible words in a message
    unnecessary_words_quantity_checks = 0
    while unnecessary_words_quantity_checks != len(unnecessary_words):
        # creating an array for each word separately
        word_from_unnecessary_words = []
        for i in unnecessary_words[unnecessary_words_quantity_checks]:
            word_from_unnecessary_words.append(i)
        # check for the presence of a word in a message
        quantity_checks = 0
        new_array_without_unnecessary_words = []
        while quantity_checks != len(memory_array):
            # the case when there is no word in the array
            if (memory_array[quantity_checks] != word_from_unnecessary_words[0]) or (
                    quantity_checks > (len(memory_array) - len(word_from_unnecessary_words))):
                new_array_without_unnecessary_words.append(memory_array[quantity_checks])
            # the case when the first letter of the checked word is found and a check is required
            else:
                correct_spare_quantity_checks = 0
                spare_quantity_checks = quantity_checks
                while correct_spare_quantity_checks != len(word_from_unnecessary_words):
                    # coincidence count
                    if memory_array[spare_quantity_checks] == word_from_unnecessary_words[
                        correct_spare_quantity_checks]:
                        correct_spare_quantity_checks += 1
                        # deleting the detected word and then replacing it
                        if correct_spare_quantity_checks == len(word_from_unnecessary_words):
                            quantity_checks = spare_quantity_checks
                            new_array_without_unnecessary_words.append(",")
                    # case where at least one mismatch is allowed
                    else:
                        new_array_without_unnecessary_words.append(memory_array[quantity_checks])
                        break
                    spare_quantity_checks += 1
            quantity_checks += 1
        # updating a message without unnecessary context
        memory_array = new_array_without_unnecessary_words
        unnecessary_words_quantity_checks += 1

    # work check
    print(''.join(memory_array))


# detecting a prefix in context
def analysis_of_a_message_for_prefixes(msg):
    # creating a character-by-character array from a message
    check_for_prefixes = []
    for i in msg:
        check_for_prefixes.append(i)
    # creating a loop to iterate over and find all prefixes in the message
    prefix_check = 0
    while prefix_check != len(bot_prefixes):
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
        # magic
        if prefix_found == True:
            prefix_check = len(bot_prefixes)
            simplifying_texts_for_defining_basic_commands(check_for_prefixes)
        # repeat the operation if one of the prefixes did not match
        else:
            prefix_check += 1


bot_prefixes = ["owl", "сова"]
union_words = ["but", "and", "а", "но", "и"]
punctuation_marks = [".", ",", ";", "!", "?"]
msg = str.lower(input("-->"))
analysis_of_a_message_for_prefixes(msg)

# Authors of the projects:
# 1-MachnevEgor_https://vk.com/machnev_egor
# 2-DmitryShalimov_https://vk.com/lookatstat
# Contacts in email:
# 1-mea90608744@gmail.com
# 2-dmitriy-shalimov@yandex.ru