import sys
from collections import defaultdict



sys.setrecursionlimit(100_000)


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



with open(f'test.in', 'r') as f:
    for j in range(1, 19):
        graph = defaultdict(list)
        with open(f'test{j:02d}.in', 'r') as f:
            m = int(f.readline())
            for i in range(m):
                v, e = f.readline().split()
                graph[v].append(e)
                graph[e].append(v)
            print(graph_is_eulerian(graph))
            print(f.readline())

# n = int(input())
# g5 = defaultdict(list)
# for i in range(n):
#     v, e = map(int, input().split())
#     g5[v].append(e)
# print(graph_is_eulerian(g5))