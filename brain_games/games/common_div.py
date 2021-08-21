import random
import math

INTRO = 'Find the greatest common divisor of given numbers.'


def game_question():
    x = random.randint(1, 50)
    y = random.randint(1, 50)
    problem = str(x) + ' ' + str(y)
    result = str(math.gcd(x, y))
    return problem, result
