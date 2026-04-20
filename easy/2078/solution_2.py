# https://leetcode.com/problems/two-furthest-houses-with-different-colors

from typing import List

def maxDistance(colors: List[int]) -> int:
    n = len(colors)

    for i in range(n - 1):
        if colors[i] != colors[n - 1]:
            return n - 1 - i
        if colors[n - 1 - i] != colors[0]:
            return n - 1 - i
    return 0

colors = [1,1,1,6,1,1,1]
print(maxDistance(colors))

colors = [1,8,3,8,3]
print(maxDistance(colors))