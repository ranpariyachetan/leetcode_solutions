# https://leetcode.com/problems/construct-product-matrix

from typing import List

# Solution using brute force. Time complexity is O(m*n) and space complexity is O(m*n)
# This solution will give TLE for large inputs. We can optimize it using prefix product and suffix product.
def constructProductMatrix(grid: List[List[int]]) -> List[List[int]]:
    m = len(grid)
    n = len(grid[0])
    result = [[1] * n for _ in range(m)]

    product = 1
    for i in range(m):
        for j in range(n):
            product *= grid[i][j]


    for i in range(m):
        for j in range(n):
            result[i][j] = (product // grid[i][j]) % 12345

    return result

grid = [[1,2],[3,4]]

print(constructProductMatrix(grid))

grid = [[12345],[2],[1]]

print(constructProductMatrix(grid))