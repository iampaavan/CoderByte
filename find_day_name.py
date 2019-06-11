import calendar
import datetime


def find_day(date):
    day = datetime.datetime.strptime(date, '%d-%m-%Y').weekday()
    return calendar.day_name[day]


print(f"Day: {find_day('14-05-1992')}")
print(f"Day: {find_day('21-07-1991')}")

