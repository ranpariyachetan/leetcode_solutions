

from typing import List
from functools import cmp_to_key

import emoji
def maxStability(n: int, edges: List[List[int]], k: int) -> int:

    if len(edges) < n - 1:
        return -1
    
    mustedges = []
    optedges = []

    parents = list(range(n))

    mustMinStatbility = 200000
    result = -1
    for edge in edges:
        if edge[3] == 1:
            mustedges.append(edge)
        else:
            optedges.append(edge)

    if len(mustedges) > n - 1:
            return -1
    
    def comparator(a, b):
        return b[2] - a[2]

    def findParent(x):
        if parents[x] != x:
            parents[x] = findParent(parents[x])
        return parents[x]

    def union(x, y):
        s1 = findParent(x)
        s2 = findParent(y)

        parents[s1] = s2
    selectedInit =0
    for edge in mustedges:
        s = edge[0]
        d = edge[1]
        w = edge[2]
        if findParent(s) != findParent(d):
            union(s,d)
            mustMinStatbility = min(mustMinStatbility, w)
            selectedInit += 1
        else:
            return -1

    originalParents = parents[:]
    optedges = sorted(optedges, key = cmp_to_key(comparator))

    left = 0
    right = mustMinStatbility

    while left < right:
        mid = left +((right - left + 1) >> 1)
        doubledCount =0
        selected = selectedInit
        parents = originalParents[:]
        for edge in optedges:
            s = edge[0]
            d = edge[1]
            w = edge[2]
            if findParent(s) != findParent(d):
                if w >= mid:
                    union(s,d)
                    selected += 1
                elif doubledCount <k and w * 2 >= mid:
                    doubledCount += 1
                    union(s,d)
                    selected += 1
                else:
                    break

            if selected == n - 1:
                break
        if selected != n - 1:
            right = mid - 1
        else:
            result = left = mid

    return result

def print_test_result(input, expected, actual):
     print(f"{emoji.emojize(':check_mark_button:') if expected == actual else emoji.emojize(':cross_mark:')} Input = {input}, Expected = {expected}, Actual = {actual}")

n = 3
edges =[[0,1,2,1],[1,2,3,0]]
k = 1

print_test_result((n, edges, k), 2, maxStability(n, edges, k))  # expected = 2

n = 3
edges = [[0,1,4,0],[1,2,3,0],[0,2,1,0]]
k = 2

print_test_result((n, edges, k), 6, maxStability(n, edges, k))  # expected = 6


n = 3
edges = [[0,1,1,1],[1,2,1,1],[2,0,1,1]]
k = 0

print_test_result((n, edges, k), -1, maxStability(n, edges, k))  # expected = -1

n = 5
edge = [[2,0,68643,1],[1,0,31681,1],[4,2,44760,1],[3,4,19034,1],[1,4,24247,0]]
k = 2

print_test_result((n, edge, k), 19034, maxStability(n, edge, k))  # expected = 19034

n = 2
edges = [[0,1,87487,0]]
k = 0

print_test_result((n, edges, k), 87487, maxStability(n, edges, k))  # expected = 87487