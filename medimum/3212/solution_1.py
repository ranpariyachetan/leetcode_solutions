# https://leetcode.com/problems/count-submatrices-with-equal-frequency-of-x-and-y

from git import List

def numberOfSubmatrices(grid: List[List[str]]) -> int:
    m, n = len(grid), len(grid[0])
    ans = 0

    for r in range(0, m):
        for c in range(n):
            x_cnt = y_cnt = 0

            if grid[r][c] == 'X':
                x_cnt += 1
            elif grid[r][c] == 'Y':
                y_cnt += 1

            if r > 0:
                x_cnt += grid[r - 1][c][0]
                y_cnt += grid[r - 1][c][1]
            if c > 0:
                x_cnt += grid[r][c - 1][0]
                y_cnt += grid[r][c - 1][1]

            if r > 0 and c > 0:
                x_cnt -= grid[r - 1][c - 1][0]
                y_cnt -= grid[r - 1][c - 1][1]

            if x_cnt >= 1 and x_cnt == y_cnt:
                ans += 1

            grid[r][c] = (x_cnt, y_cnt)
    return ans


grid = [["X","Y","."],["Y",".","."]]

print(numberOfSubmatrices(grid))

grid = [["X","X"],["X","Y"]]

print(numberOfSubmatrices(grid))