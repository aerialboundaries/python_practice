# Comma Code

def comma(list):
    length = len(list)
    for i in range(length):
        print(list[i] + ',', end='')

    print('and ' + list[-1])

spam = ['apples', 'bananas', 'tofu', 'cats']
comma(spam)


