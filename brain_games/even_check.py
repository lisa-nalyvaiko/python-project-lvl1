#!/usr/bin/env python
import prompt
import random


def even_number():
    """Prompts user to guess the number.

    Returns:
        string and answer prompt.
    """
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Welcome,{name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')

    tries = 0
    while tries < 3:
        number = random.randint(0, 100)
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')
        if number % 2 == 0:
            # print('number is even')
            if answer.lower() == 'yes':
                print('Correct!')
                tries += 1
                continue
            else:
                print("'no' is wrong answer ;(. " + \
                      f"Correct answer was 'yes'.\nLet's try again, {name}!")
                break
        else:
            # print('number is odd')
            if answer.lower() == 'yes':
                print("'yes' is wrong answer ;(. " + \
                      f"Correct answer was 'no'.\nLet's try again, {name}!")
                break
            else:
                print('Correct!')
                tries += 1
                continue
    if tries == 3:
        print(f'Congratulations, {name}!')
