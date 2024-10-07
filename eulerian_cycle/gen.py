import networkx as nx
import random






for i in range(1, 19):
    with open(f'test{i:02d}.in', 'w') as f:
        x = random.randint(1, 2)
        if x == 1:
            a = nx.gnm_random_graph(random.randint(2, 50_000),random.randint(2,30_000))
        if x == 2:
            a = nx.barbell_graph(random.randint(2, 800),random.randint(2, 10))
            if random.randint(0, 1):
                a = nx.eulerize(a)
        print(a)
        m = a.edges()
        print(len(m), file=f)
        for elem in m:
            print(*elem, file=f)
        print(nx.is_eulerian(a), file=f)
#524911
#49710