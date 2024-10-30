def prims_alg(graph, n):
    taken = [False] * n
    min_weights = [float('+inf')] * n
    min_weights[0] = 0
    for _ in range(n):
        u = min((v for v in range(n) if not taken[v]), key=lambda v: min_weights[v])
        taken[u] = True
        for v in range(n):
            if 0 < graph[u][v] < min_weights[v] and not taken[v]:
                min_weights[v] = graph[u][v]

    return sum(min_weights)


if __name__ == '__main__':
    n = int(input())
    print(prims_alg([[int(i) for i in input().split()] for _ in range(n)], n))
