# https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-i

from typing import List

def assignEdgeWeigths(edges: List[List[int]]) -> int:
    MOD = 10**9 + 7

    n = len(edges) + 1
    graph = [[] for _ in range(n + 1)]

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    def dfs(g, x, f) -> int:
        max_depth = 0
        for y in g[x]:
            if y == f:
                continue
            max_depth = max(max_depth, dfs(g, y, x) + 1)
        return max_depth

    max_depth = dfs(graph, 1, 0)

    return pow(2, max_depth - 1, MOD)


edges = [[1,2]]
print(assignEdgeWeigths(edges))

edges = [[1,2],[1,3],[3,4],[3,5]]
print(assignEdgeWeigths(edges))

edges = [[3,2],[2,1]]
print(assignEdgeWeigths(edges))