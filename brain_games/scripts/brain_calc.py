#!/usr/bin/env python
"""Brain Calc Game"""

from brain_games.engine import run_game
from brain_games.games.calc import calc_question


def main():
    """Greets user and runs "brain calc" game.

    Returns:
        string and user name prompt.
    """
    return run_game(calc_question)


if __name__ == '__main__':
    main()
