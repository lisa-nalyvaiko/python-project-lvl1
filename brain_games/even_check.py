#!/usr/bin/env python
import prompt
import random


def game_question():
    """Returns generated number and correct answer"""
    number = random.randint(1, 100)
    result = 'yes' if is_even(number) else 'no'
    return number, result


def is_even(number):
    """Returns whether generated number is even"""
    return number % 2 == 0


def even_number():
    """Prompts user to guess the number.

    Returns:
        string and answer prompt.
    """
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Welcome,{name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    number_of_rounds = 3
    counter = 0
    while counter < number_of_rounds:
        number, result = game_question()
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')
        if answer.lower() == result:
            print('Correct!')
            counter += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{result}'.\nLet's try again, {name}!")
            return
        if counter == number_of_rounds:
            print(f'Congratulations, {name}!')
