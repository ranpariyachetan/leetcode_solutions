# https://leetcode.com/problems/minimize-hamming-distance-after-swap-operations

from typing import List

def minimumHammingDistance(source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
    n = len(source)
    parent = list(range(n))
    
    def find(x: int) -> int:
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x: int, y: int) -> None:
        rootX = find(x)
        rootY = find(y)
        if rootX != rootY:
            parent[rootY] = rootX

    for x, y in allowedSwaps:
        union(x, y)
    groups = {}
    for i in range(n):
        root = find(i)
        if root not in groups:
            groups[root] = []
        groups[root].append(i)
    distance = 0
    for indices in groups.values():
        source_count = {}
        target_count = {}
        for idx in indices:
            source_count[source[idx]] = source_count.get(source[idx], 0) + 1
            target_count[target[idx]] = target_count.get(target[idx], 0) + 1
        for num in source_count:
            if num in target_count:
                distance += max(0, source_count[num] - target_count[num])
            else:
                distance += source_count[num]
    return distance

source = [1,2,3,4]
target = [2,1,4,5]
allowedSwaps = [[0,1],[2,3]]
print(minimumHammingDistance(source, target, allowedSwaps))

source = [1,2,3,4]
target = [1,3,2,4]
allowedSwaps = []
print(minimumHammingDistance(source, target, allowedSwaps))