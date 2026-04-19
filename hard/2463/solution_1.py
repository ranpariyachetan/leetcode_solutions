# https://leetcode.com/problems/minimum-total-distance-traveled

from functools import lru_cache
from typing import List
from math import inf

def minimumTotalDistance(robot: List[int], factory: List[List[int]]) -> int:
    robot.sort()
    factory.sort(key=lambda x: x[0])
    n, m = len(robot), len(factory)
    memo = {}
    def dp(i:int, j:int) -> int:
        if i == n:
            return 0
        if j == m:
            return inf
        
        if (i, j) in memo:
            return memo[(i, j)]
        
        pos, limit = factory[j]
        res = dp(i, j + 1)

        dist = 0
        for k in range(1, min(limit, n - i) + 1):
            dist += abs(robot[i + k - 1] - pos)
            res = min(res, dist + dp(i + k, j + 1))

        memo[(i, j)] = res
        return res
                       
    return dp(0, 0)

robot = [0,4,6]
factory = [[2,2],[6,2]]
print(minimumTotalDistance(robot, factory))

robot = [1,-1]
factory = [[-2,1],[2,1]]
print(minimumTotalDistance(robot, factory))

robot = [9,11,99,101]
factory = [[10,1],[7,1],[14,1],[100,1],[96,1],[103,1]]
print(minimumTotalDistance(robot, factory))
