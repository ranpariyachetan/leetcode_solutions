# https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid

from typing import List

def hasValidPath(grid: List[List[int]]) -> bool:
    m, n = len(grid), len(grid[0])

    visited = [[False] * n for _ in range(m)]

    street_map = {
        1: ["left", "right"],
        2: ["up", "down"],
        3: ["left", "down"],
        4: ["right", "down"],
        5: ["left", "up"],
        6: ["right", "up"],
        }

    flow_map = {
        "left": "right",
        "up": "down",
        "right": "left",
        "down": "up",
    }

    dirs = {"up": [-1, 0], "down": [1, 0], "left": [0, -1], "right": [0, 1]}

    def dfs(x, y):
        if x == m - 1 and y == n - 1:
            return True
        
        if visited[x][y]:
            return False

        visited[x][y] = True

        # Every cell can be exited via two directions. We need to check both of them.

        dir_1 = street_map[grid[x][y]][0]
        dir_2 = street_map[grid[x][y]][1]

        # For both the directions, we need to check if the next cell has a street that can be entered from the current direction.
        newx, newy = x + dirs[dir_1][0], y + dirs[dir_1][1]

        if newx >= 0 and newx < m and newy >= 0 and newy < n and flow_map[dir_1] in street_map[grid[newx][newy]]:
            if dfs(newx, newy):
                return True

        newx, newy = x + dirs[dir_2][0], y + dirs[dir_2][1]

        if newx >= 0 and newx < m and newy >= 0 and newy < n and flow_map[dir_2] in street_map[grid[newx][newy]]:
            if dfs(newx, newy):
                return True

        return False
    
    return dfs(0, 0)

grid = [[2,4,3],[6,5,2]]
print(hasValidPath(grid))

grid = [[2,4,3],[6,5,1]]
print(hasValidPath(grid))

grid = [[1,2,1],[1,2,1]]
print(hasValidPath(grid))

grid = [[6,1,3],[4,1,5]]
print(hasValidPath(grid))