# https://leetcode.com/problems/maximum-walls-destroyed-by-robots

from bisect import bisect_left, bisect_right
from functools import lru_cache
from typing import List
import emoji

def maxWalls(robots: List[int], distance: List[int], walls: List[int]) -> int:
    robots = sorted(zip(robots, distance), key=lambda x: x[0])
    walls.sort()

    ranges = []

    n = len(robots)

    def count_walls(left, right):
        if left > right:
            return 0
        return bisect_right(walls, right) - bisect_left(walls, left)
    
    @lru_cache(None)
    def dp(i, covered_right):
        if i == n:
            return 0
        
        best = 0

        for interval in ranges[i]:
            left, right = interval
            newLeft = max(left, covered_right + 1)
            add = count_walls(newLeft, right)
            best = max(best, add + dp(i + 1, max(covered_right, right)))
        return best

    for i in range(n):
        robot, dist = robots[i]

        left_bound = robot - dist
        right_bound = robot + dist

        if i - 1 >= 0:
            left_bound = max(left_bound, robots[i-1][0] + 1)
        if i + 1 < n:
            right_bound = min(right_bound, robots[i + 1][0] - 1)

        left_interval = (left_bound, robot)
        right_interval = (robot, right_bound)

        ranges.append((left_interval, right_interval))

    return dp(0, -10**18)


def print_test_result(input, expected, actual):
    print(f"{emoji.emojize(':check_mark_button:') if expected == actual else emoji.emojize(':cross_mark:')} Input = {input}, Expected = {expected}, Actual = {actual}")

robots = [10,2]
distance = [5,1]
walls = [5,2,7]

expected = 3
print_test_result((robots, distance, walls), expected, maxWalls(robots, distance, walls))

robots = [4]
distance = [3]
walls = [1, 10]
expected = 1
print_test_result((robots, distance, walls), expected, maxWalls(robots, distance, walls))

robots = [1,2]
distance = [100,1]
walls = [10]

expected = 0
print_test_result((robots, distance, walls), expected, maxWalls(robots, distance, walls))

robots = [17,59,32,11,72,18]
distance = [5,7,6,5,2,10]
walls = [17,25,33,29,54,53,18,35,39,37,20,14,34,13,16,58,22,51,56,27,10,15,12,23,45,43,21,2,42,7,32,40,8,9,1,5,55,30,38,4,3,31,36,41,57,28,11,49,26,19,50,52,6,47,46,44,24,48]
expected = 37
print_test_result((robots, distance, walls), expected, maxWalls(robots, distance, walls))
