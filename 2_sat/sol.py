from collections import defaultdict


def two_sat(clauses):
    graph = defaultdict(set)
    for clause in clauses:
        if len(clause) == 2:
            i, j = clause
            graph[-i].add(j)
            graph[-j].add(i)
        else:
            i = clause[0]
            graph[-i].add(i)
    scc_list = kosaraju(graph)
    for seq in scc_list:
        for item in seq:
            if -item in seq:
                return False
    return True


def dfs(vertex, graph, used, stack):
    used.add(vertex)
    for neighbor in graph[vertex]:
        if neighbor not in used:
            dfs(neighbor, graph, used, stack)
    stack.append(vertex)


def transpose_graph(graph):
    reversed_graph = defaultdict(set)
    for node in graph:
        for neighbor in graph[node]:
            reversed_graph[neighbor].add(node)
    return reversed_graph


def make_component(vertex, graph, visited, component):
    visited.add(vertex)
    component.append(vertex)
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            make_component(neighbor, graph, visited, component)


def go_through_all_components(graph, used, stack):
    for vertex in list(graph):
        if vertex not in used:
            dfs(vertex, graph, used, stack)


def kosaraju(graph):
    stack = []
    used = set()
    go_through_all_components(graph, used, stack)
    transposed_graph = transpose_graph(graph)
    scc_list = []
    used = set()
    while stack:
        node = stack.pop()
        if node not in used:
            component = []
            make_component(node, transposed_graph, used, component)
            scc_list.append(component)
    return scc_list


sat = []
m = int(input())
for _ in range(m):
    s = [int(i) for i in input().split()]
    sat.append(s)
print('Possible' if two_sat(sat) else 'Impossible')