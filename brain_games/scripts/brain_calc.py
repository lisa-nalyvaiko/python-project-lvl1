#!/usr/bin/env python

from brain_games.engine import run_game
from brain_games.games.calc import calc_question


def main():
    """Greets user and runs "check for even" game.

    Returns:
        string and user name prompt.
    """
    return run_game(calc_question)


if __name__ == '__main__':
    main()
