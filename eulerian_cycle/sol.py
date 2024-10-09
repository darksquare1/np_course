import sys
from collections import defaultdict

sys.setrecursionlimit(10_000)


def dfs(vertex, graph, visited):
    visited.add(vertex)
    for v in graph[vertex]:
        if v not in visited:
            dfs(v, graph, visited)


def graph_is_connected(graph):
    visited = set()
    start = list(graph.keys())[0]
    dfs(start, graph, visited)
    for v in graph:
        if v not in visited:
            return False
    return True


def graph_is_eulerian(graph):
    if not graph_is_connected(graph):
        return False
    for v in graph:
        if len(graph[v]) % 2 != 0:
            return False
    return True

g = defaultdict(list)
for i in range(int(input())):
    v, e = map(int, input().split())
    g[v].append(e)
    g[e].append(v)
print('YES' if graph_is_eulerian(g) else 'NO')
