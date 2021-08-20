#!/usr/bin/env python
import random

INTRO = 'Answer "yes" if the number is even, otherwise answer "no".'


def game_question():
    """Returns generated number and correct answer"""
    question = random.randint(1, 100)
    result = 'yes' if is_even(question) else 'no'

    return question, result


def is_even(number):
    """Returns whether generated number is even"""
    return number % 2 == 0
