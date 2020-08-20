# Authors of the project:
# 1-MachnevEgor_https://vk.com/machnev_egor
# 2-DmitryShalimov_https://vk.com/lookatstat
# Contacts in email:
# 1-meb.official.com@gmail.com
# 2-dmitriy-shalimov@yandex.ru

from phrasesDatabase import VariationPhrases as VariationPhrases

# Everything that happens in message processing:
# 1) detecting a prefix in context
# 2) checking the message for links and further rewriting
# 3) removing unnecessary words that play the role of punctuation marks
# 4) deleting words with low contextual significance from the message
# 5.1) step to remove all spaces from the message
# 5.2) step to remove duplicate punctuation marks
# 5.3) step to remove punctuation mark if it is at the beginning of the message
# 6) distribution of commands

# main arrays
start_of_https_links = ["https://www.youtube.com/"]
union_words = [",but ", " and ", ", а", ", но", ", и", " и "]
not_influencing_words = [", excuse me,", ", excuse me", "excuse me,", "excuse me", ", please,", ", please", "please,",
                         "please", ", pray,", ", pray", "pray,", "pray", ", пожалуйста,", ", пожалуйста", "пожалуйста,",
                         "пожалуйста", ", желательно,", ", желательно", "желательно,", "желательно", ", быстро,",
                         ", быстро", "быстро,", "быстро", ", быстрей,", ", быстрей", "быстрей,", "быстрей",
                         ", побыстрей,", ", побыстрей", "побыстрей,", "побыстрей", ", oh,", ", oh", "oh ,", "oh", "'"]
punctuation_marks = [".", ",", ";", "!", "?"]


# 6) distribution of commands
def distribution_of_commands_to_parts_of_the_array(memory_array):
    # getting started only if there is some context
    if memory_array != []:
        # loop processing a message and dividing it into commands
        quantity_checks = 0
        new_command_array = []
        while (quantity_checks != (len(memory_array) - 1)):
            if memory_array[quantity_checks] in punctuation_marks:
                msg_commands.append(''.join(new_command_array))
                new_command_array = []
            else:
                new_command_array.append(memory_array[quantity_checks])
            quantity_checks += 1
        # the case when the command does not have a punctuation mark at the end
        if quantity_checks >= (len(memory_array) - 1 - 1):
            while quantity_checks != len(memory_array):
                new_command_array.append(memory_array[quantity_checks])
                quantity_checks += 1
            msg_commands.append("".join(new_command_array))


# 5.3) step to remove punctuation mark if it is at the beginning of the message
def remove_punctuation_mark_if_it_is_at_the_beginning_of_the_message(memory_array):
    # getting started only if there is some context
    if memory_array != []:
        # a condition under which a punctuation mark was detected and rewriting is required
        if (memory_array[0] in punctuation_marks):
            new_array = []
            quantity_checks = 0
            while quantity_checks != (len(memory_array) - 1):
                new_array.append(memory_array[quantity_checks + 1])
                quantity_checks += 1
            memory_array = new_array
    # sending processing to the next stage
    distribution_of_commands_to_parts_of_the_array(memory_array)


# 5.2) step to remove duplicate punctuation marks
def removing_duplicate_punctuation_marks(memory_array):
    # loop to find punctuation marks within a sentence
    quantity_checks = 0
    new_array_duplicate_punctuation_marks = []
    while quantity_checks != len(memory_array):
        # one of the punctuation marks found
        if memory_array[quantity_checks] in punctuation_marks:
            imaginary_quantity_checks = quantity_checks
            while imaginary_quantity_checks != len(memory_array):
                if memory_array[imaginary_quantity_checks] not in punctuation_marks:
                    quantity_checks = imaginary_quantity_checks - 1
                    new_array_duplicate_punctuation_marks.append(memory_array[quantity_checks])
                    break
                imaginary_quantity_checks += 1
        # punctuation mark not found
        else:
            new_array_duplicate_punctuation_marks.append(memory_array[quantity_checks])
        quantity_checks += 1
    memory_array = new_array_duplicate_punctuation_marks
    # sending processing to the next stage
    remove_punctuation_mark_if_it_is_at_the_beginning_of_the_message(memory_array)


# 5.1) step to remove all spaces from the message
def removing_all_spaces_from_a_message(memory_array):
    # loop to find spaces and remove them
    quantity_checks = 0
    new_array_without_spaces = []
    while quantity_checks != len(memory_array):
        if memory_array[quantity_checks] != " ":
            new_array_without_spaces.append(memory_array[quantity_checks])
        quantity_checks += 1
    memory_array = new_array_without_spaces
    # sending processing to the next stage
    removing_duplicate_punctuation_marks(memory_array)


# 4) deleting words with low contextual significance from the message
def checking_the_text_for_the_presence_of_other_unnecessary_words(memory_array):
    # going through all possible words in a message
    words_quantity_checks = 0
    while words_quantity_checks != len(not_influencing_words):
        # creating an array for each word separately
        word_from_array_words = []
        for i in not_influencing_words[words_quantity_checks]:
            word_from_array_words.append(i)
        # check for the presence of a word in a message
        quantity_checks = 0
        new_array_without_not_influencing_words = []
        while quantity_checks != len(memory_array):
            # the case when there is no word in the array
            if (memory_array[quantity_checks] != word_from_array_words[0]) or (
                    quantity_checks > (len(memory_array) - len(word_from_array_words))):
                new_array_without_not_influencing_words.append(memory_array[quantity_checks])
            # the case when the first letter of the checked word is found and a check is required
            else:
                correct_spare_quantity_checks = 0
                spare_quantity_checks = quantity_checks
                while correct_spare_quantity_checks != len(word_from_array_words):
                    # coincidence count
                    if memory_array[spare_quantity_checks] == word_from_array_words[
                        correct_spare_quantity_checks]:
                        correct_spare_quantity_checks += 1
                        # deleting the detected word and then replacing it
                        if correct_spare_quantity_checks == len(word_from_array_words):
                            quantity_checks = spare_quantity_checks
                    # case where at least one mismatch is allowed
                    else:
                        new_array_without_not_influencing_words.append(memory_array[quantity_checks])
                        break
                    spare_quantity_checks += 1
            quantity_checks += 1
        # updating a message without unnecessary context
        memory_array = new_array_without_not_influencing_words
        words_quantity_checks += 1
    # sending processing to the next stage
    removing_all_spaces_from_a_message(memory_array)


# 3) removing unnecessary words that play the role of punctuation marks
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
    # sending processing to the next stage
    checking_the_text_for_the_presence_of_other_unnecessary_words(memory_array)


# 2) checking the message for links and further rewriting
def checking_for_links_in_the_message(memory_array):
    # loop to iterate over all possible start of links
    links_quantity_checks = 0
    while links_quantity_checks != len(start_of_https_links):
        # creating an array of letters to start of link to be searched for in the message
        link_from_links = []
        for i in start_of_https_links[links_quantity_checks]:
            link_from_links.append(i)
        # search cycle for matches
        quantity_checks = 0
        new_array_without_links = []
        while quantity_checks != len(memory_array):
            # condition when no match
            if (memory_array[quantity_checks] != link_from_links[0]) or (
                    quantity_checks > (len(memory_array) - len(link_from_links))):
                new_array_without_links.append(memory_array[quantity_checks].lower())
            # case where there is the slightest coincidence
            else:
                correct_spare_quantity_checks = 0
                spare_quantity_checks = quantity_checks
                while correct_spare_quantity_checks != len(link_from_links):
                    # full match check
                    if memory_array[spare_quantity_checks] == link_from_links[
                        correct_spare_quantity_checks]:
                        correct_spare_quantity_checks += 1
                        # the case when the beginning of a full link is found in the text
                        if correct_spare_quantity_checks == len(link_from_links):
                            # search for the full content of the link and its end
                            new_array_WITH_links = []
                            while spare_quantity_checks != len(memory_array):
                                # the case when the coordinate of the end of the link is found through a space or punctuation
                                if (memory_array[spare_quantity_checks] == " ") or (
                                        memory_array[spare_quantity_checks] == ","):
                                    while quantity_checks != spare_quantity_checks:
                                        new_array_WITH_links.append(memory_array[quantity_checks])
                                        quantity_checks += 1
                                    msg_links.append(''.join(new_array_WITH_links))
                                    new_array_without_links.append(",")
                                    break
                                # the case when the link goes to the end of the message
                                elif spare_quantity_checks == (len(memory_array) - 1):
                                    while quantity_checks <= spare_quantity_checks:
                                        new_array_WITH_links.append(memory_array[quantity_checks])
                                        if quantity_checks == (len(memory_array) - 1):
                                            msg_links.append("".join(new_array_WITH_links))
                                            new_array_without_links.append(",")
                                            break
                                        quantity_checks += 1
                                spare_quantity_checks += 1
                    # the case when there was only a little coincidence
                    else:
                        new_array_without_links.append(memory_array[quantity_checks].lower())
                        break
                    spare_quantity_checks += 1
            quantity_checks += 1
        # recording new content and replacing old
        memory_array = new_array_without_links
        links_quantity_checks += 1
    # sending processing to the next stage
    simplifying_texts_for_defining_basic_commands(memory_array)


# 1) detecting a prefix in context
def start_message_analysis(input_msg):
    # global output variables
    global addressing_the_bot
    addressing_the_bot = bool(False)
    global prefix_number
    prefix_number = 0
    global msg_commands
    msg_commands = []
    global msg_links
    msg_links = []
    # creating a general array with prefixes
    global bot_prefixes
    bot_prefixes = []
    for number_of_prefixes_processed in VariationPhrases.ctx_bot_prefixes:
        bot_prefixes.append(number_of_prefixes_processed)
    for number_of_prefixes_processed in VariationPhrases.ru_bot_prefixes:
        bot_prefixes.append(number_of_prefixes_processed)
    for number_of_prefixes_processed in VariationPhrases.eng_bot_prefixes:
        bot_prefixes.append(number_of_prefixes_processed)
    # creating a character-by-character array from a message
    check_for_prefixes = []
    for i in input_msg:
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
            if check_for_prefixes[quantity_checks].lower() == prefix_from_prefixes[correct_quantity_checks]:
                correct_quantity_checks += 1
                if correct_quantity_checks == len(prefix_from_prefixes):
                    prefix_found = True
                    break
            else:
                correct_quantity_checks = 0
            quantity_checks += 1
        # magic
        if prefix_found == True:
            prefix_number = prefix_check
            prefix_check = len(bot_prefixes)
            addressing_the_bot = True
            checking_for_links_in_the_message(check_for_prefixes)
        # repeat the operation if one of the prefixes did not match
        else:
            prefix_check += 1

# Authors of the project:
# 1-MachnevEgor_https://vk.com/machnev_egor
# 2-DmitryShalimov_https://vk.com/lookatstat
# Contacts in email:
# 1-meb.official.com@gmail.com
# 2-dmitriy-shalimov@yandex.ru
