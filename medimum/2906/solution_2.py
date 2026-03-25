# https://leetcode.com/problems/construct-product-matrix

from typing import List

# This is optimized solution using prefix product and suffix product. Time complexity is O(m*n) and space complexity is O(m*n)
def constructProductMatrix(grid: List[List[int]]) -> List[List[int]]:
    m = len(grid)
    n = len(grid[0])
    result = [[1] * n for _ in range(m)]
    MOD = 12345

    product = 1
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            result[i][j] = product
            product = (product * grid[i][j]) % MOD

    product = 1
    for i in range(m):
        for j in range(n):
            result[i][j] = (result[i][j] * product) % MOD
            product = (product * grid[i][j]) % MOD

    return result

grid = [[1,2],[3,4]]

print(constructProductMatrix(grid))

grid = [[12345],[2],[1]]

print(constructProductMatrix(grid))

grid = [[3,2,5],[6,4,3],[6,3,1]]

print(constructProductMatrix(grid))
# [1, 2, 3]
# [3, 4, 5]
# [5, 6, 7]

# [1, 2, 6]
# [3, 1 ,1]
# [15, 1, 1]