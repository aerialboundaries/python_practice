#!/usr/bin/env python

# phoneAndEmail.py - Fids phone numbers and email addresses on the clipboard.

import pyperclip, re

phoneRegex = re.compile(r'''
    (\d{3}|\(\d{3}\))?      # area code
    (\s|-|\.)?              # separator
    (\d{3})                 # first 3 digits
    (\s|-|\.)?              # separator
    (\d{4})                 # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extesion
''', re.VERBOSE)

# Create email regex
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+       # username
    @                       # @ simbol
    [a-zA-Z0-9.-]+          # domain name
    (\.[a-zA-Z]{2,4})       # dot-something
)''', re.VERBOSE)

# Find matches in clipboard text.
text = str(pyperclip.paste())

matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[0], groups[2], groups[4]])
    if groups[7] != '':
        phoneNum += ' x' + groups[7]
    matches.append(phoneNum)

for groups in emailRegex.findall(text):
    matches.append(groups[0])

# Copy results to the clipboard.
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copies to clipboard:')
    print('\n'.join(matches))
else:
    print('Nophone numbers or email addresses found.')
