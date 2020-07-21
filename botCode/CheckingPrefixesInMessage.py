def analysis_of_a_message_for_prefixes(msg, bot_prefixes):
    check_for_prefixes = []
    for i in msg:
        check_for_prefixes.append(i)
    len_bot_prefixes = len(bot_prefixes)
    prefix_check = 0
    while len_bot_prefixes != 0:
        prefix_from_prefixes = []
        for i in bot_prefixes[prefix_check]:
            prefix_from_prefixes.append(i)
        correct_quantity_checks = 0
        len_prefix_from_prefixes = len(prefix_from_prefixes)
        while len_prefix_from_prefixes != 0:
            if check_for_prefixes[correct_quantity_checks] == prefix_from_prefixes[correct_quantity_checks]:
                len_prefix_from_prefixes -= 1
                correct_quantity_checks += 1
            else:
                len_prefix_from_prefixes = 0
        print(len_prefix_from_prefixes)
        print(correct_quantity_checks)
        if (len_prefix_from_prefixes == 0) and (correct_quantity_checks != 0):
            len_bot_prefixes = 0
            print(prefix_from_prefixes, 'найдено соответствие', check_for_prefixes)
            counter_of_processed_characters = 0
            for i in check_for_prefixes:
                counter_of_processed_characters += 1
                if i == (" "):
                    cycle_count = len(check_for_prefixes) - counter_of_processed_characters
                    translated_characters_count = 0
                    final_array = []
                    while cycle_count != 0:
                        final_array.append(
                            check_for_prefixes[(translated_characters_count + counter_of_processed_characters)])
                        translated_characters_count += 1
                        cycle_count -= 1
                    break
                else:
                    final_array = []
        else:
            len_bot_prefixes -= 1
            print(prefix_from_prefixes, 'соответствий не найдено', check_for_prefixes)
            final_array = []
        prefix_check += 1



    print("final_array = ", final_array)
    print(' '.join(final_array))







bot_prefixes = ["owl", "сова"]
msg = str.lower(input("-->"))
analysis_of_a_message_for_prefixes(msg, bot_prefixes)






# # Authors of the projects:
# # 1-MachnevEgor_https://vk.com/machnev_egor
# # 2-DmitryShalimov_https://vk.com/lookatstat
# # Contacts in email:
# # 1-mea90608744@gmail.com
# # 2-dmitriy-shalimov@yandex.ru
#
# bot_prefixes = ["owl ", "сова "]
# msg = str.lower(input("-->"))
#
# check_for_prefixes = []
# for i in msg:
#     check_for_prefixes.append(i)
# len_bot_prefixes = len(bot_prefixes)
# prefix_check = 0
# while len_bot_prefixes != 0:
#     prefix_from_prefixes = []
#     for i in bot_prefixes[prefix_check]:
#         prefix_from_prefixes.append(i)
#     correct_quantity_checks = 0
#     len_prefix_from_prefixes = len(prefix_from_prefixes)
#     while len_prefix_from_prefixes != 0:
#         if check_for_prefixes[correct_quantity_checks] == prefix_from_prefixes[correct_quantity_checks]:
#             len_prefix_from_prefixes -= 1
#             correct_quantity_checks += 1
#         else:
#             len_prefix_from_prefixes = 0
#     print(len_prefix_from_prefixes)
#     print(correct_quantity_checks)
#     if (len_prefix_from_prefixes == 0) and (correct_quantity_checks != 0):
#         len_bot_prefixes = 0
#         print(prefix_from_prefixes, 'найдено соответствие', check_for_prefixes)
#         counter_of_processed_characters = 0
#         for i in check_for_prefixes:
#             counter_of_processed_characters += 1
#             if i == (" "):
#                 cycle_count = len(check_for_prefixes) - counter_of_processed_characters
#                 translated_characters_count = 0
#                 final_array = []
#                 while cycle_count != 0:
#                     final_array.append(
#                         check_for_prefixes[(translated_characters_count + counter_of_processed_characters)])
#                     translated_characters_count += 1
#                     cycle_count -= 1
#                 break
#             else:
#                 final_array = []
#     else:
#         len_bot_prefixes -= 1
#         print(prefix_from_prefixes, 'соответствий не найдено', check_for_prefixes)
#         final_array = []
#     prefix_check += 1
#
# print("final_array = ", final_array)
#
# # Authors of the projects:
# # 1-MachnevEgor_https://vk.com/machnev_egor
# # 2-DmitryShalimov_https://vk.com/lookatstat
# # Contacts in email:
# # 1-mea90608744@gmail.com
# # 2-dmitriy-shalimov@yandex.ru
