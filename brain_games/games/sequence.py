import random

INTRO = 'What number is missing in the progression?'


def game_question():
    start = random.randint(1, 50)
    step = random.randint(1, 10)
    length = 10
    sequence = [start]
    for i in range(length-1):
        sequence.append(sequence[-1]+step)
    guess = random.randint(1, 10)
    result = str(sequence[guess-1])
    sequence[guess-1] = '..'
    problem = ', '.join(map(str, sequence))
    return problem, result
