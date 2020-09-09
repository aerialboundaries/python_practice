#!/usr/bin/env python3

# Mad Libs
import re

def change(target):
    if target == 'ADJECTIVE':
       ADJECTIVE = input('Enter an adjective: \n')
       return ADJECTIVE
    elif target == 'NOUN':
        NOUN = input('Enter a noun: \n')
        return NOUN
    elif target == 'VERB':
        VERB = input('Enter a verb: \n')
        return VERB
    elif target == 'ADVERB':
        ADVERB = input('Enter a adverb: \n')
        return ADVERB

baseFile = open('9-madbase.txt')
baseText = baseFile.read()
madRegex = re.compile(r'ADJECTIVE|NOUN|VERB|ADVERVE')
madMatch= madRegex.findall(baseText)
times = len(madMatch)
for i in range(times):
    mo = madRegex.search(baseText)
    target = mo.group()
    baseText = baseText.replace(target, change(target), 1)

print(baseText)

newtext = open('9-revised.txt', 'w')
newtext.write(baseText)
baseFile.close()
newtext.close()

