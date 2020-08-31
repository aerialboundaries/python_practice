#!/bin/bash/ python

import re

nameRegex = re.compile(r'''(
    (Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|cats|baseballs)\.
    )''', re.IGNORECASE|re.VERBOSE)

mo = nameRegex.findall('''
Alice eats apples.
Bob pets cats.
Carol throws baseballs
Alice throws Apples.
BOB EATS CATS.
RoboCop eats apples.
ALICE THROWS FOOTBALLS.
Carol eats 7cats.
''')

for i in mo:
    print(i[0])
