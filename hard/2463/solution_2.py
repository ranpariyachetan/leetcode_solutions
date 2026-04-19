# https://leetcode.com/problems/minimum-total-distance-traveled

from functools import lru_cache
from typing import List
from math import inf

def minimumTotalDistance(robot: List[int], factory: List[List[int]]) -> int:
    robot.sort()
    factory.sort(key=lambda x: x[0])
    n, m = len(robot), len(factory)

    dp = [[inf] * (m + 1) for _ in range(n + 1)]
    for j in range(m + 1):
        dp[0][j] = 0
    
    for j in range(1, m + 1):
        pos, limit = factory[j - 1]
        for i in range(n + 1):
            dp[i][j] = dp[i][j - 1] # Skip this factory
            dist = 0
            for k in range(1, min(limit, i) + 1):
                dist += abs(robot[i - k] - pos)
                dp[i][j] = min(dp[i][j], dist + dp[i - k][j - 1])

    return dp[n][m]

robot = [0,4,6]
factory = [[2,2],[6,2]]
print(minimumTotalDistance(robot, factory))

robot = [1,-1]
factory = [[-2,1],[2,1]]
print(minimumTotalDistance(robot, factory))

robot = [9,11,99,101]
factory = [[10,1],[7,1],[14,1],[100,1],[96,1],[103,1]]
print(minimumTotalDistance(robot, factory))
