# https://leetcode.com/problems/count-submatrices-with-top-left-element-and-sum-less-than-k

from git import List

def countSubmatrices(grid: List[List[int]], k: int) -> int:
    m, n = len(grid), len(grid[0])
    ans = 0

    for r in range(0, m):
        sum = 0
        for c in range(n):
            if r > 0:
                grid[r][c] += grid[r-1][c]
            sum += grid[r][c]
            if sum <= k:
                ans += 1

    return ans

grid = [[7,6,3],[6,6,1]]
k = 18

print(countSubmatrices(grid, k))

grid = [[7,7,10,9],[10,5,10,3]]
k = 54
print(countSubmatrices(grid, k))

grid = [[7,2,9],[1,7,0],[2,7,6]]
k = 20
print(countSubmatrices(grid, k))