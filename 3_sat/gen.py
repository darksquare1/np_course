import random

random.seed(4)

CLAUSE_LENGTH_CHOICES = [3] * 100 + [1] * 5 + [2] * 5
M = 15
N = 5


def generate_files(number=18):
    for index in range(1, number + 1):
        with open(f'{index:02d}.in', 'w') as file:
            m = random.randint(1, M)
            print(m, file=file)
            three_sat = '\n'.join(generate_clauses(m))
            print(three_sat, file=file)


def generate_variable(n):
    return random.choice([-1, 1]) * random.randint(1, n)


def generate_clauses(n):
    for _ in range(n):
        clause_length = random.choice(CLAUSE_LENGTH_CHOICES)
        if clause_length == 3:
            clause = f'{generate_variable(N)} {generate_variable(N)} {generate_variable(N)}'
        elif clause_length == 2:
            clause = f'{generate_variable(N)} {generate_variable(N)}'
        else:
            clause = str(generate_variable(N))
        yield clause


generate_files(15)