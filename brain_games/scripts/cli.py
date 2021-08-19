#!/usr/bin/env python
"""Script with welcome function."""
import prompt


def welcome_user():
    """Welcome message and user name prompt.

    Returns: string and input.
    """
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Welcome,{name}!')
