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
    wrong = f"'no' is wrong answer ;(. Correct answer was 'yes'.\nLet's try again, {name}!"
    wrong_odd = f"'yes' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, {name}!"
    right = 'Correct!'
    win = f'Congratulations, {name}!'
    counter = 0
    while counter < 3:
        number = random.randint(1, 100)
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')
        if number % 2 == 0:
            # print('number is even')
            if answer.lower() == 'yes':
                print(right)
                counter += 1
                continue
            else:
                print(wrong)
                break
        else:
            # print('number is odd')
            if answer.lower() == 'yes':
                print(wrong_odd)
                break
            else:
                print(right)
                counter += 1
                continue
    if counter == 3:
        print(win)
