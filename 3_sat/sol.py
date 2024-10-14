n = int(input())
first_clause = list(map(int,input().split()))
my_sets = [{c} for c in first_clause]

for _ in range(n - 1):
    temp_sets = []
    current_clause = list(map(int, input().split()))

    for s in my_sets:
        for literal in current_clause:
            if -literal not in s:
                new_set = s.copy()
                new_set.add(literal)
                temp_sets.append(new_set)

    my_sets = temp_sets

print('Possible' if my_sets else 'Impossible')