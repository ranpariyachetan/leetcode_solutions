# https://leetcode.com/problems/count-submatrices-with-equal-frequency-of-x-and-y

from git import List

def numberOfSubmatrices(grid: List[List[str]]) -> int:
    m, n = len(grid), len(grid[0])
    ans = 0

    px = [0] * n
    py = [0] * n

    for r in range(0, m):
        x_cnt = y_cnt = 0
        for c in range(n):
            if grid[r][c] == 'X':
                x_cnt += 1
            elif grid[r][c] == 'Y':
                y_cnt += 1

            px[c] += x_cnt
            py[c] += y_cnt

            if px[c] == py[c] and px[c] > 0:
                ans += 1
    return ans


grid = [["X","Y","."],["Y",".","."]]

print(numberOfSubmatrices(grid))

grid = [["X","X"],["X","Y"]]

print(numberOfSubmatrices(grid))