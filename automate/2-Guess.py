# 2-Guess the number game

import random

print('I am thinking of a number between 1 and 20.')
secretNumber = random.randint(1, 20)

for i in range(5):
    print('Take a guess.')

    try:
        guess = int(input())

    except ValueError:
        print('Please input integer')

    if guess < secretNumber:
        print('Your guess is too low.')

    elif guess > secretNumber:
        print('Your guess is too high')

    else:
        break

if guess == secretNumber:
    print('Good job! You guessed my number in {0} times'.format(i + 1))
else:
    print('Nope, I was thinking of {}'.format(secretNumber))
