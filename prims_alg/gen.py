import random
from itertools import combinations, groupby

random.seed(0)


class Graph:
    def __init__(self):
        self.edges = []
        self.nodes = []

    def add_nodes(self, nodes):
        self.nodes.extend(nodes)

    def add_edge(self, edge):
        self.edges.append(edge)


def gnp_random_connected_graph(n, p):
    edges = combinations(range(n), 2)
    G = Graph()
    G.add_nodes(range(n))
    for _, node_edges in groupby(edges, key=lambda x: x[0]):
        node_edges = list(node_edges)
        random_edge = random.choice(node_edges)
        G.add_edge(random_edge)
        for e in node_edges:
            if random.random() < p:
                G.add_edge(e)
    return G


def generate_adjacency_matrix(n):
    g = gnp_random_connected_graph(n, 0.5)

    edges = set(g.edges)
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if (i, j) in edges:
                matrix[i][j] = matrix[j][i] = random.randint(1, 1000)
    return matrix


def gen_files(files_num):
    for i in range(3, files_num + 4):
        with open(f'{i:02d}.in', 'w') as f:
            n = random.randint(2, 1000)
            matrix = generate_adjacency_matrix(n)
            print(n, file=f)
            for row in matrix:
                print(*row, file=f)


if __name__ == '__main__':
    gen_files(15)
