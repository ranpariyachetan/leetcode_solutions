# https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid

from typing import List
def minOperations(grid: List[List[int]], x: int) -> int:
    m, n = len(grid), len(grid[0])
    nums = []
    answer = 0

    for i in range(m):
        for j in range(n):
            nums.append(grid[i][j])

    nums.sort()

    median = nums[len(nums) // 2]

    for num in nums:
        if num % x != median % x:
            return -1
        answer += abs(num - median) // x

    return answer

grid = [[2, 4], [6, 8]]
x = 2
print(minOperations(grid, x))

grid = [[1, 5], [2, 3]]
x = 1
print(minOperations(grid, x))

grid = [[1, 2], [3, 4]]
x = 2
print(minOperations(grid, x))

grid  = [[141,105,69,273,681,105,933,417,309],[921,657,945,717,885,57,453,921,897],[681,345,657,177,897,609,465,801,429],[681,993,741,885,105,981,477,249,921],[369,885,945,537,45,861,381,345,417],[849,849,477,513,297,609,561,177,801],[561,417,129,585,621,561,261,153,501],[249,777,969,249,357,393,93,321,573],[525,813,381,909,825,297,681,345,813]]
x = 12
print(minOperations(grid, x))