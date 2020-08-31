#!/usr/bin/env python

# Project 7-3 Strong Regex Version of the strip() Method

import re

testWord = 'aabbcc-abc-aabbcc'


def spritRegex(word, remove=' '):
    stripRegexL = re.compile(r'(^[' + remove + ']*)')
    stripRegexR = re.compile(r'([' + remove + ']*$)')
    result = stripRegexL.sub('', word)
    result = stripRegexR.sub('', result)
    print(result)

spritRegex(testWord, 'ab')
