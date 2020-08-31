#!/bin/bash/ python

import re

nameRegex = re.compile(r'[A-Z]\w*\sWatanabe')
mo = nameRegex.findall('Haruto Watanabe, Alice Watanabe, Robocop Watanabe, haruto Watanabe, Mr. Watanabe, Watanabe, Haruto watanabe')

print(mo)
