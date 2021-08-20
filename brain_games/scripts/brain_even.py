#!/usr/bin/env python
"""Brain Even game"""

from brain_games.engine import run_game
from brain_games.games.even_check import game_question


def main():
    """Greets user and runs "brain even" game."""
    return run_game(game_question)


if __name__ == '__main__':
    main()
