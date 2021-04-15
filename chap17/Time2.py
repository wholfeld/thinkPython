from __future__ import annotations


class Time2:
    """Represents the time of day."""
    def __init__(self, hour:int=0, minute:int=0, second:int=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self:Time2)->Time2:
        return f'{self.hour:02}:{self.minute:02}:{self.second:02}'

    def __add__(self:Time2, other:Time2)->Time2:
        if isinstance(other, Time2):
            return self.add_time(other)
        else:
            return self.increment(other)
    
    def __radd__(self:Time2, other:int)->Time2:
        return self.increment(other)

    def add_time(self, other):
        seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)
    

    def print_time(self):
        print(f'{self.hour:02}:{self.minute:02}:{self.second:02}')

    def time_to_int(self)->int:
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    def increment(self, seconds: int) -> Time2:
        seconds = self.time_to_int() + seconds
        return int_to_time(seconds)



def int_to_time(seconds: int) -> Time2:
    time = Time2()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

if __name__ == '__main__':
    start = Time2(9, 45)
    duration = Time2(1, 35)
    print(start + duration) # should be 11:20:00
    print(start + 1337) # should be 10:07:17
    print(1337 + start ) # should be 10:07:17

    t1 = Time2(7, 43)
    t2 = Time2(7, 41)
    t3 = Time2(7, 37)
    total = sum([t1, t2, t3])
    print(total) # should be 23:01:00


# start = Time2(9, 45)
# # start.hour = 9
# # start.minute = 45
# # start.second = 00
# inc_time = start.increment(69)
# print(inc_time)

