import random

random.seed(0)

CLAUSE_LENGTH_CHOICES = [2] * 90 + [1] * 5
M = 100_000
N = 100_000


def generate_files(number=18):
    for index in range(1, number + 1):
        with open(f'{index:02d}.in', 'w') as file:
            m = random.randint(1, M)
            print(m, file=file)
            two_sat = '\n'.join(generate_clauses(m))
            print(two_sat, file=file)


def generate_variable(n):
    return random.choice([-1, 1]) * random.randint(1, n)


def generate_clauses(n):
    for _ in range(n):
        clause_length = random.choice(CLAUSE_LENGTH_CHOICES)
        yield f'{generate_variable(N)} {generate_variable(N)}' if clause_length == 2 else str(generate_variable(N))


generate_files(17)