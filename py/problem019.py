"""Counting Sundays
Problem 19
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
"""

monthlengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
date = {}
date[1900] = {}
date[1900][0] = 1
lastyear = 1900
lastmonth = 0
for year in xrange(1900, 2001):
    if year != 1900:
        date[year] = {}
    for month in xrange(12):
        if year != 1900 or month != 0:
            date[year][month] = (date[lastyear][lastmonth] + monthlengths[(month + 11) % 12]) % 7
            if month == 2 and year % 4 == 0 and year != 1900:
                date[year][month] += 1
                date[year][month] %= 7
    lastyear = year
    lastmonth = month
answer = 0
for year in xrange(1901, 2001):
    for month in xrange(12):
        if date[year][month] == 0:
            print year,month
            answer += 1
print date[1900]
print answer
