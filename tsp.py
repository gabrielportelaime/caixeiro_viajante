from sys import maxsize
from itertools import permutations
V = 4
def tsp(graph, s):
    vertex = []
    for i in range(V):
        if i != s:
            vertex.append(i)
    min_cost = maxsize
    next_permutation = permutations(vertex)
    for i in next_permutation:
        current_cost = 0
        k = s
        for j in i:
            current_cost += graph[k][j]
            k = j
        current_cost += graph[k][s]
        min_cost = min(min_cost, current_cost)
    return min_cost

graph =[[0, 1, 2, 5], 
        [1, 0, 6, 4], 
        [2, 6, 0, 4], 
        [5, 4, 4, 0]]
s = 0
print(tsp(graph, s))