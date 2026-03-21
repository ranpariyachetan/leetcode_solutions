# https://leetcode.com/problems/flip-square-submatrix-vertically

from typing import List

def reverseSubMatrix(grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
    p = 1
    for i in range(x, x + k//2):
        for j in range(y, y + k):
            grid[i][j], grid[x + k - p][j] = grid[x + k - p][j], grid[i][j]
        p += 1

    return grid


grid = [[6,16,14],[1,2,19],[14,17,15],[18,7,6],[14,12,5]]
x, y, k = 2, 1, 2
print(reverseSubMatrix(grid, x, y, k))

grid = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
x, y, k = 1, 0, 3
print(reverseSubMatrix(grid, x, y, k))

grid = [[3,4,2,3],[2,3,4,2]]
x, y, k = 0, 2, 2
print(reverseSubMatrix(grid, x, y, k))