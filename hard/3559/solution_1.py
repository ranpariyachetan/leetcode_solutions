# https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-ii

from typing import List
from collections import defaultdict, deque

def assignEdgeWeights(edges: List[List[int]], queries: List[List[int]]) -> List[int]:
    MOD = 10**9 + 7
    n = len(edges) + 1

    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    LOG = 17
    depth = [0] * (n + 1)
    # up[k][v] = 2^k-th ancestor of v; 0 is sentinel (no node)
    up = [[0] * (n + 1) for _ in range(LOG)]

    visited = [False] * (n + 1)
    visited[1] = True
    queue = deque([1])
    while queue:
        node = queue.popleft()
        for neighbor in adj[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                depth[neighbor] = depth[node] + 1
                up[0][neighbor] = node
                queue.append(neighbor)

    for k in range(1, LOG):
        for v in range(1, n + 1):
            up[k][v] = up[k - 1][up[k - 1][v]]

    def lca(u: int, v: int) -> int:
        if depth[u] < depth[v]:
            u, v = v, u
        diff = depth[u] - depth[v]
        for k in range(LOG):
            if (diff >> k) & 1:
                u = up[k][u]
        if u == v:
            return u
        for k in range(LOG - 1, -1, -1):
            if up[k][u] != up[k][v]:
                u = up[k][u]
                v = up[k][v]
        return up[0][u]

    pow2 = [1] * (n + 1)
    for i in range(1, n + 1):
        pow2[i] = pow2[i - 1] * 2 % MOD

    answer = []
    for u, v in queries:
        l = lca(u, v)
        d = depth[u] + depth[v] - 2 * depth[l]
        answer.append(pow2[d - 1] if d > 0 else 0)

    return answer

edges = [[1,2],[1,3],[3,4],[3,5]]
queries = [[1,4],[3,4],[2,5]]

print(assignEdgeWeights(edges, queries))