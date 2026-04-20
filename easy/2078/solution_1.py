# https://leetcode.com/problems/two-furthest-houses-with-different-colors

from typing import List

def maxDistance(colors: List[int]) -> int:
    answer = 0
    n = len(colors)

    for i in range(n):
        for j in range(n - 1, i, -1):
            if colors[i] != colors[j]:
                answer = max(answer, j - i)
                break

    return answer

colors = [1,1,1,6,1,1,1]
print(maxDistance(colors))

colors = [1,8,3,8,3]
print(maxDistance(colors))