import datetime

users = [{'name': "Bill", 'birthday': datetime.datetime(year=1990, month=12, day=31)},
         {'name': "William", 'birthday': datetime.datetime(year=2005, month=10, day=11)},
         {'name': "Marie", 'birthday': datetime.datetime(year=1999, month=8, day=26)},
         {'name': "Max", 'birthday': datetime.datetime(year=1998, month=7, day=5)},
         {'name': "Elena", 'birthday': datetime.datetime(year=2000, month=5, day=23)},
         {'name': "Pavel", 'birthday': datetime.datetime(year=1996, month=4, day=24)}]

print(users)


def get_birthdays_per_week(users):
    today = datetime.date.today()
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    if today.weekday() == 0:
        start_week = today - datetime.timedelta(days=6)
    else:
        start_week = today - datetime.timedelta(days=today.weekday() - 1)
        print(start_week)
    end_week = start_week + datetime.timedelta(days=6)

    print("Birthdays for the week of {} to {}".format(start_week, end_week))

    for i in range(7):
        day = start_week + datetime.timedelta(days=i)
        print(weekdays[i] + ':', end=' ')
        for user in users:
            if user['birthday'].day == day.day and user['birthday'].month == day.month:
                if i == 0 and user['birthday'].weekday() > 4:
                    print(" {}".format(user['name']))
                else:
                    print("{}".format(user['name']))
        print()


get_birthdays_per_week(users)
