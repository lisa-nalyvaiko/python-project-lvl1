#!/usr/bin/env python
"""Main script."""


from brain_games.scripts.cli import welcome_user


def main():
    """Make game intro.

    Returns:
        string and user name prompt.
    """
    return welcome_user()


if __name__ == '__main__':
    main()
