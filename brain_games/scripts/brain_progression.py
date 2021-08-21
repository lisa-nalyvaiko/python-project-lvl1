#!/usr/bin/env python
"""Brain Even game"""

from brain_games.engine import run_game
from brain_games.games import sequence


def main():
    """Greets user and runs "brain even" game."""
    return run_game(sequence)


if __name__ == '__main__':
    main()
