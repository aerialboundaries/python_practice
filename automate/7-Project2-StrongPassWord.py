#!/usr/bin/env python

# Project 7-2 Strong Password

import re

passWord = 'dA2dsG4a'

lengthRegex = re.compile(r'\w{8,}')
upperRegex = re.compile(r'[A-Z]')
lowerRegex = re.compile(r'[a-z]')
digitRegex = re.compile(r'\d')

def isStrong(word):
    strong = True
    if lengthRegex.search(word) == None:
        print('Pass word should be at least 8 characters')
        strong = False
    if upperRegex.search(word) == None:
        print('Pass word should contain uppercase')
        strong = False
    if lowerRegex.search(word) == None:
        print('Pass word should contain lowercase')
        strong = False
    if digitRegex.search(word) == None:
        strong = False
        print('Pass word should contain digit')
    if strong == True:
        print('The password %s is strong.' % (word))

isStrong(passWord)
