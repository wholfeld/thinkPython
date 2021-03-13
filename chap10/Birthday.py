from random import randint

def duplicate_birthday():
    birthdays = []
    for i in range(23):
        birthdays.append(randint(1, 365))
    birthdays.sort()
    for i in range(1, len(birthdays)):
        if birthdays[i] == birthdays[i - 1]:
            return True
    return False

def run_birthdays():
    runs = 0.0
    dups = 0
    for i in range(1000):
        runs += 1
        if duplicate_birthday():
            dups += 1
    return dups/runs

print(run_birthdays())
