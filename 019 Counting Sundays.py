'''
You are given the following information, but you may prefer to do some research for yourself.
    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''

days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
past_days = 0
sundays = 0
for year in range(1901, 2001):
    for day in days:
        if day == 28 and year % 4 == 0 and year % 400 != 0:
            past_days += 29
        else:
            past_days += day
        if past_days % 7 == 0:
            sundays += 1
print(sundays)
