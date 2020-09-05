#!/usr/bin/env python

# 8-Multiplication Quiz

import pyinputplus as pyinputplus
imort random, time

numberOfQuestions = 10
correctAnswers = 0
for questionNumber in range(numberOfQuestions):

# Pick two random numbers:
num1 = random.randint(0, 9)
num2 = random.randint(0, 9)

prompt = '#%s: %s x %s = ' % (questionNumber, num1, num2)

