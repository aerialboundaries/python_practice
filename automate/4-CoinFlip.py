# Coin Flip Streaks

import random
numberOfStreaks = 0
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tail' values.
    test100 = []

    for i in range(100):
        if random.randint(0, 1) == 0:
            face = 'H'
        else:
            face = 'T'

        test100.append(face)

    # Code that checks if there is a streak of 6heads or tails in a row.
    for j in range(5, len(test100)):
        for k in range(5):
            if test100[j] != test100[j - k]:
                streak = False
            else:
                streak = True
    
    if streak == True:
        numberOfStreaks += 1

print('Streaks = %s' %numberOfStreaks)
print('Chance of streak: %s%%' %(numberOfStreaks /(100*10000)))
