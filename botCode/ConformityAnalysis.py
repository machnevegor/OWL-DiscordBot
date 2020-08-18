# Authors of the project:
# 1-MachnevEgor_https://vk.com/machnev_egor
# 2-DmitryShalimov_https://vk.com/lookatstat
# Contacts in email:
# 1-mea90608744@gmail.com
# 2-dmitriy-shalimov@yandex.ru

# analyzing of all commands for a request
def find_command_matches(msg_command, prepared_questions_matrix):
    # update declaring variable
    global coincidence_of_the_command
    coincidence_of_the_command = []
    # splitting part of all commands into letter-by-letter parts
    letter_by_letter_command = []
    for command_letter_by_letter_overwrite in "".join(msg_command):
        letter_by_letter_command.append(command_letter_by_letter_overwrite)
    # matrix movement
    for quantity_matched_arrays_in_matrix in range(len(prepared_questions_matrix)):
        # motion throught an array in a matrix
        for quantity_questions_array_checks in range(
                len(prepared_questions_matrix[quantity_matched_arrays_in_matrix])):
            # splitting part of all questions into letter-by-letter parts
            question_from_prepared_questions_array = []
            for question_letter_by_letter_overwrite in prepared_questions_matrix[quantity_matched_arrays_in_matrix][
                quantity_questions_array_checks]:
                question_from_prepared_questions_array.append(question_letter_by_letter_overwrite)
            # analysis for coincidence
            correct_quantity_checks = 0
            for quantity_letters_passed_in_command in range(len(letter_by_letter_command)):
                if letter_by_letter_command[quantity_letters_passed_in_command] == \
                        question_from_prepared_questions_array[correct_quantity_checks]:
                    correct_quantity_checks += 1
                    if correct_quantity_checks == len(question_from_prepared_questions_array):
                        # writing the array number, if before that it did not match the commands
                        if quantity_matched_arrays_in_matrix not in coincidence_of_the_command:
                            coincidence_of_the_command.append(quantity_matched_arrays_in_matrix)
                        # go to the next
                        break
                # other cases with small coincidences
                else:
                    correct_quantity_checks = 0

# Authors of the project:
# 1-MachnevEgor_https://vk.com/machnev_egor
# 2-DmitryShalimov_https://vk.com/lookatstat
# Contacts in email:
# 1-mea90608744@gmail.com
# 2-dmitriy-shalimov@yandex.ru