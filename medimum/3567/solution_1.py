# https://leetcode.com/problems/minimum-absolute-difference-in-sliding-submatrix

from git import List


def minAbsDiff(grid: List[List[int]], k:int) -> List[List[int]]:
    m, n = len(grid), len(grid[0])
    ans = [[0] * (n - k + 1) for _ in range(m - k + 1)]

    for r in range(0, m - k + 1):
        for c in range(0, n - k + 1):
            submat = []
            for i in range(r, r + k):
                for j in range(c, c + k):
                    submat.append(grid[i][j])
            submat.sort()
            min_diff = float('inf')
            for i in range(1, len(submat)):
                if submat[i] != submat[i - 1]:
                    min_diff = min(min_diff, abs(submat[i] - submat[i - 1]))
            if min_diff == float('inf'):
                min_diff = 0
            ans[r][c] = min_diff
    return ans


grid = [[1,8],[3,-2]]
k = 2

print(minAbsDiff(grid, k))

grid = [[3,-1]]
k = 1
print(minAbsDiff(grid, k))

grid = [[1,-2,3],[2,3,5]]
k = 2
print(minAbsDiff(grid, k))