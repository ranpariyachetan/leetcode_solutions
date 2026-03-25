# https://leetcode.com/problems/equal-sum-grid-partition-i

from typing import List

def canPartition(grid: List[List[int]]) -> bool:
    m, n = len(grid), len(grid[0])
    # total_sum = sum(sum(row) for row in grid)

    temp = [[[0, 0] for _ in range(n)] for _ in range(m)]
    row_sum = 0
    col_sum = 0
    for i in range(0, m):
        for j in range(0, n):
            row_sum += grid[i][j]
            temp[i][j][0] = row_sum

    for j in range(0, n):
        for i in range(0, m):
            col_sum += grid[i][j]
            temp[i][j][1] = col_sum

    total_sum = temp[m - 1][n - 1][0]

    if total_sum % 2 != 0:
        return False
            
    for i in range(m):
        if temp[i][n - 1][0] == total_sum // 2:
            return True
        
    for j in range(n):
        if temp[m - 1][j][1] == total_sum // 2:
            return True

    return False

grid = [[1,3],[2,4]]

print(canPartition(grid))

grid = [[1,2],[3,4]]
print(canPartition(grid))

grid = [[1,4],[2,3]]
print(canPartition(grid))

grid = [[9753,4621,3652],[3003,4050,433]]

print(canPartition(grid))

grid = [[1,1,1]]

print(canPartition(grid))