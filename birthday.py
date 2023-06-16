import datetime
import random

users = []
today = datetime.datetime(year=2023, month=6, day=13)


# today = datetime.datetime.now()

def pers_gen(people_num: int):
    """Create dictionaries with information about the user in the form of name and birthday
     and add them to the list of users."""

    name = ["Devid", "Kavin", "Lisy", "Taya", "Brogan", "Jakub", "Mariyah"]
    for i in range(people_num):
        year = random.randint(1960, 2005)
        month = random.randint(1, 12)
        day = None
        max_days = None

        this_month = datetime.datetime(year=year, month=month, day=1)
        if month == 12:
            next_month = datetime.datetime(year=year + 1, month=1, day=1)
            max_days = int(str(next_month - this_month).split(" ")[0])
        else:
            next_month = datetime.datetime(year=year, month=month + 1, day=1)
            max_days = int(str(next_month - this_month).split(" ")[0])

        day = random.randint(1, max_days)
        birthday = datetime.datetime(year=year, month=month, day=day)
        users.append({"name": random.choice(name), "birthday": birthday})


def get_birthdays_per_week(users: list, today: datetime):
    """Generate a messages about the days of the week
     and the names of those who have a birthday on those days."""

    days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    day_of_week = today.strftime('%A')
    #print("Today", today.date(), day_of_week)
    diff = None
    birthday_this_year = None
    birthdey_list = []
    min_days = None
    max_days = None

    if day_of_week != "Monday":
        min_days = 0
        max_days = 6
    else:
        min_days = -2
        max_days = 4

    for user in users:
        # if the birthday is 29.02 and this year we do not have this date, change mount and day
        try:
            birthday_this_year = datetime.datetime(year=today.year, month=user["birthday"].month,
                                                   day=user["birthday"].day)
        except:
            birthday_this_year = datetime.datetime(year=today.year, month=3, day=1)

        # if diff = 0 day we got [00:00:00], in this situation we got an error
        try:
            diff = int(str(birthday_this_year - today).split(" ")[0])
        except ValueError:
            diff = 0

        if min_days <= diff <= max_days:
            print(user["name"], birthday_this_year.date(), birthday_this_year.strftime('%A'))
            burthday_day = birthday_this_year.strftime('%A')
            if burthday_day == "Saturday" or burthday_day == "Sunday":
                burthday_day = "Monday"
            birthdey_list.append({burthday_day: user["name"]})

    for day in days[2:]:
        everyday_list = []
        for birth in birthdey_list:
            if day == list(birth.keys())[0]:
                everyday_list.append(birth[day])
        if len(everyday_list) > 0:
            print(f"{day}: {', '.join(everyday_list)}")


def main():
    pers_gen(5000)
    get_birthdays_per_week(users, today)


if __name__ == "__main__":
    main()
