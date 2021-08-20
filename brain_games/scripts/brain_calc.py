#!/usr/bin/env python
"""Brain Calc Game"""

from brain_games.engine import run_game
from brain_games.games import calc


def main():
    """Greets user and runs "brain calc" game."""
    return run_game(calc)


if __name__ == '__main__':
    main()
