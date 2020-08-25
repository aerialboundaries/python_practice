# 5 - Character Count

import pprint
message = 'It was a bright cold day in April, ad the clocks were striking thirten.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count)
