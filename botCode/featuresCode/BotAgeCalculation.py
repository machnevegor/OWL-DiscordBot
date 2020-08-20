# Authors of the project:
# 1-MachnevEgor_https://vk.com/machnev_egor
# 2-DmitryShalimov_https://vk.com/lookatstat
# Contacts in email:
# 1-meb.official.com@gmail.com
# 2-dmitriy-shalimov@yandex.ru

from random import randint as randint
import datetime as datetime

# bot creation date
year_of_foundation = 2020
foundation_month = 7
foundation_day = 17

# the current date
now_time = datetime.datetime.today()
now_time_year = now_time.year
now_time_month = now_time.month
now_time_day = now_time.day
# nuances number systems
if now_time.month < foundation_month:
    now_time_year -= 1
    now_time_month += 12
if now_time.day < foundation_day:
    now_time_month -= 1
    now_time_day += 30


def ru_years_old():
    # creating an empty response
    global ru_bot_age
    ru_bot_age = []
    # fool trap
    if ((now_time_year - year_of_foundation) >= 0) and ((now_time_month - foundation_month) >= 0) and (
            (now_time_day - foundation_day) >= 0):
        # creating an array with age
        bot_age = []
        # year(s)
        bot_age.append(now_time_year - year_of_foundation)
        time_difference = [(now_time_year - year_of_foundation)]
        if time_difference[-1] == 1:
            bot_age.append("год,")
        elif (time_difference[-1] == 2) or (time_difference[-1] == 3) or (time_difference[-1] == 4):
            bot_age.append("года,")
        else:
            bot_age.append("лет,")
        # month(s)
        bot_age.append(now_time_month - foundation_month)
        time_difference = [(now_time_month - foundation_month)]
        if time_difference[-1] == 1:
            bot_age.append("месяц")
        elif (time_difference[-1] == 2) or (time_difference[-1] == 3) or (time_difference[-1] == 4):
            bot_age.append("месяца")
        else:
            bot_age.append("месяцев")
        # union word
        bot_age.append("и")
        # day(s)
        bot_age.append(now_time_day - foundation_day)
        time_difference = [(now_time_day - foundation_day)]
        if time_difference[-1] == 1:
            bot_age.append("день")
        elif (time_difference[-1] == 2) or (time_difference[-1] == 3) or (time_difference[-1] == 4):
            bot_age.append("дня")
        else:
            bot_age.append("дней")
        # final answer
        response_randomizer = randint(0, 1)
        if response_randomizer == 0:
            ru_bot_age = ("Меня создали ровно ", " ".join(str(i) for i in bot_age), " назад)")
        elif response_randomizer == 1:
            ru_bot_age = ("Мне уже ", " ".join(str(i) for i in bot_age), ")")
        ru_bot_age = ("".join(ru_bot_age))


def eng_years_old():
    # creating an empty response
    global eng_bot_age
    eng_bot_age = []
    # fool trap
    if ((now_time_year - year_of_foundation) >= 0) and ((now_time_month - foundation_month) >= 0) and (
            (now_time_day - foundation_day) >= 0):
        # creating an array with age
        bot_age = []
        # year(s)
        bot_age.append(now_time_year - year_of_foundation)
        if (now_time_year - year_of_foundation) == 1:
            bot_age.append("year,")
        else:
            bot_age.append("years,")
        # month(s)
        bot_age.append(now_time_month - foundation_month)
        if (now_time_month - foundation_month) == 1:
            bot_age.append("month,")
        else:
            bot_age.append("months")
        # union word
        bot_age.append("and")
        # day(s)
        bot_age.append(now_time_day - foundation_day)
        if (now_time_day - foundation_day) == 1:
            bot_age.append("day,")
        else:
            bot_age.append("days")
        # final answer
        response_randomizer = randint(0, 1)
        if response_randomizer == 0:
            eng_bot_age = ("I was created ", " ".join(str(i) for i in bot_age), " ago)")
        elif response_randomizer == 1:
            eng_bot_age = ("I am ", " ".join(str(i) for i in bot_age), " old)")
        eng_bot_age = ("".join(eng_bot_age))

# Authors of the project:
# 1-MachnevEgor_https://vk.com/machnev_egor
# 2-DmitryShalimov_https://vk.com/lookatstat
# Contacts in email:
# 1-meb.official.com@gmail.com
# 2-dmitriy-shalimov@yandex.ru
