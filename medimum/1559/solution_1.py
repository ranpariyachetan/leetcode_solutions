# https://leetcode.com/problems/detect-cycles-in-2d-grid
from typing import List
def containsCycle(grid: List[List[str]]) -> bool:
    m, n = len(grid), len(grid[0])

    visited = [[False] * n for _ in range(m)]

    def dfs(x, y, parentx, parenty):

        if visited[x][y]:
            return True

        visited[x][y] = True

        for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            newx, newy = x + dx, y + dy
            if newx < 0 or newx >= m or newy < 0 or newy >= n:
                continue

            if newx == parentx and newy == parenty:
                continue

            if grid[newx][newy] != grid[x][y]:
                continue

            if dfs(newx, newy, x, y):
                return True

        return False
    
    for i in range(m):
        for j in range(n):
            if not visited[i][j] and dfs(i, j, -1, -1):
                return True

    return False


grid = [["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]

print(containsCycle(grid))

grid = [["c","c","c","a"],["c","d","c","c"],["c","c","e","c"],["f","c","c","c"]]

print(containsCycle(grid))

grid = [["a","b","b"],["b","z","b"],["b","b","a"]]

print(containsCycle(grid))