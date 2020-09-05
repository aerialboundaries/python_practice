#!/usr/bin/env python

# 8-Project Sandwitch Maker

import pyinputplus as pyip


# Using inputMenu() for a bread type: wheat, white, or sourdough.
def breadType():
    prompt = 'Please input the type of bread.\n'
    response = pyip.inputMenu(['wheat', 'white', 'sourdough'], prompt=prompt)
    breadPrice = priceList[response]
    return float(breadPrice)


# Using inputMenu() for a protein type: chicken, turkey, ham, or tofu.
def proteinType():
    prompt = 'Please iinput the protein type.\n'
    response = pyip.inputMenu(['chiken', 'turkey', 'ham', 'tofu'], prompt=prompt)
    proteinPrice = priceList[response]
    return float(proteinPrice)


# Using inputYesNo() to ask if they want cheese.
def cheeseOption():
    prompt = 'Do you want cheese?\n'
    if pyip.inputYesNo(prompt) == 'yes':
        return True
    else:
        return False


# If so, using inputMenu() to ask for a cheese type: cheddar, Swiss,
# or mozzarella.
def cheeseType():
    if cheeseOption():
        prompt = 'How would you like your cheese?\n'
        response = pyip.inputMenu(['cheddar', 'swiss', 'mozzarella'])
        cheesePrice = priceList[response]
        return float(cheesePrice)
    else:
        return 0


# Using inputYesNo() to ask if they want mayo, mustard, lettuce, or tomato.
def topExtra():
    prompt = 'Would you like mayo, mustard, lettuce, or tomato?\n'
    response = pyip.inputYesNo(prompt)
    if response == 'yes':
        toppingPrice = priceList['topping']
    else:
        toppingPrice = 0
    return float(toppingPrice)


# Using inputInt() to ask how many sandwiches they want. Make sure
# this number is 1 or more.
def orderQty():
    prompt = 'How many sandwiches would you take?\n'
    response = pyip.inputInt(prompt, min=1)
    return response


# Come up with prices for each of these options, and have your program
# display a total cost after the user enters their selection.
priceList = {
    'wheat': 1.0, 'white': '1.1', 'sourdough': 1.2, 'chicken': 2.0,
    'turkey': 2.1, 'ham': 2.2, 'tofu': 2.3, 'cheddar': 0.5, 'swiss': 0.6,
    'mozzarella': 0.7, 'topping': 0.8
}

unitPrice = 0.0
unitPrice += breadType()
unitPrice += proteinType()
unitPrice += cheeseType()
unitPrice += topExtra()
totalQty = orderQty()
totalPrice = unitPrice * totalQty
print('Total amount is %0.2f dollars.' % (totalPrice))
