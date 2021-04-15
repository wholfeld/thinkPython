from datetime import date, datetime 
import calendar

class Time:
    """Represents the time of day.
    
    attributes: hour, minute, second
    """
    def __init__(self):
        pass

    # def __str__(self):

def time_to_birthday(birthday: date)-> None:
    birthday_ord = birthday.toordinal()
    time_tup = birthday.timetuple()
    birthday_ord_seconds = datetime.fromordinal(birthday_ord)
    birthday_seconds = (birthday - datetime(1970,1,1)).total_seconds()
    now_ord = date.today().toordinal()
    dif_ord = now_ord - birthday_ord
    age = dif_ord / 365.25
    future_birthday = date(date.today().year, birthday.month, birthday.day).toordinal()
    if future_birthday < now_ord:
        future_birthday = date(date.today().year + 1, birthday.month, birthday.day)
    print(f'The users age is: {age} years old.')
    days_until_birthday = future_birthday - now_ord
    dif = date.today() - birthday
    print(f'There are {days_until_birthday} days until birthday')


def current_day_print():
    current_date = datetime.now()
    day_str = calendar.day_name[current_date.weekday()]
    print(day_str)

def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time


def increment(time, seconds):
    new_time = Time()
    new_time.second = time.second
    new_time.minute = time.minute
    new_time.hour = time.hour
    new_time.second += seconds

    if new_time.second >= 60:
        new_time.second -= 60
        new_time.minute += 1

    if new_time.minute >= 60:
        new_time.minute -= 60
        new_time.hour += 1

    return new_time

def add_time(t1, t2):
    assert valid_time(t1) and valid_time(t2)
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)
    # sum = Time()
    # sum.hour = t1.hour + t2.hour
    # sum.minute = t1.minute + t2.minute
    # sum.second = t1.second + t2.second

    # if sum.second >= 60:
    #     sum.second -= 60
    #     sum.minute += 1

    # if sum.minute >= 60:
    #     sum.minute -= 60
    #     sum.hour += 1

def valid_time(time):
    if time.hour < 0 or time.minute < 0 or time.second < 0:
        return False
    if time.minute >= 60 or time.second >= 60:
        return False
    return True

def mul_time(time, multiplier):
    seconds = time_to_int(time)
    seconds *= multiplier
    return int_to_time(seconds)

def average_pace(time, distance):
    seconds = time_to_int(time)
    seconds /= distance
    return int_to_time(seconds)


time = Time()
time.hour = 11
time.minute = 59
time.second = 30

start = Time()
start.hour = 9
start.minute = 45 
start.second = 0

duration = Time()
duration.hour = 1
duration.minute = 35
duration.second = 0
# new_time = add_time(start, duration)
new_time = increment(duration, 69)
# print(new_time)
current_day_print()
birthday = date(1982, 10, 27)
time_to_birthday(birthday)
