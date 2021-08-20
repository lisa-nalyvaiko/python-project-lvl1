#!/usr/bin/env python
import prompt


def run_game(func):
    """Returns general games intro and game logic from arg function."""

    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Welcome,{name}!')

    number_of_rounds = 3
    counter = 0
    while counter < number_of_rounds:
        intro, question, result = func()
        if counter == 0:
            print(intro)
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer.lower() == result:
            print('Correct!')
            counter +=1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{result}'.\nLet's try again, {name}!")
            return
        if counter == number_of_rounds:
            print(f'Congratulations, {name}!')