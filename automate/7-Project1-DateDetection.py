#!/usr/bin/env python

# Project 7-1 Date Detection

import re

data = '29/2/2000'

dateRegex = re.compile(r'''
(\d{1,2})           # Date
(/)                 # Separator
(\d{1,2})           # Month
(/)                 # Separator
(\d{4})
''', re.VERBOSE)

day = int(dateRegex.search(data).group(1))
month = int(dateRegex.search(data).group(3))
year = int(dateRegex.search(data).group(5))

def rangeCheck(day, month, year):
    if day < 1 or day > 31:
        print('The date is out of range')
        return False

    if month < 1 or month > 12:
        print('The month is out of range')
        return False

    if year < 1000 or year > 2999:
        print('The year is out of range')
        return False

    return True


def monthDay(year, month, day):
    monthDic = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31,
        6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

    if leapYear(year):
        monthDic[2] = 29
    
    if monthDic[month] < day:
        print('Month %s has maximum %s days' % (month, monthDic[month]))
        return False

    return True


def leapYear(year):
    if year % 4 != 0:
        return False
    
    if year % 100 == 0 and year % 400 != 0:
        return False
    
    return True


if rangeCheck(day, month, year) and monthDay(year, month, day):
    print(str(day) + '/' + str(month) + '/' + str(year))
