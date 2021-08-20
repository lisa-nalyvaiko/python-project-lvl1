import random


def calc_question():
    intro = 'What is the result of the expression?'
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    ops = random.choice('+-*')

    def get_expression(a, b, op):
        if op == '+':
            z = a + b
            q = str(a) + '+' + str(b)
            return z, q
        elif op == '-':
            z = a - b
            q = str(a) + '-' + str(b)
            return z, q
        else:
            z = x * y
            q = str(a) + '*' + str(b)
            return z, q

    res, problem = get_expression(x, y, ops)
    result = str(res)
    return intro, problem, result
