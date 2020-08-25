# The collatz sequence

def collatz(number):
    if number == 1:
        return 1
    if number % 2 == 0:
        print(number // 2)
        return collatz(number // 2)
    else:
        print(number * 3 + 1)
        return collatz(number * 3 + 1)

try:
    userInput = int(input('Pleasea input integer: '))
    collatz(userInput)

except ValueError:
    print('The number must be integer')


