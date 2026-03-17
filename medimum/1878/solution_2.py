# https://leetcode.com/problems/get-biggest-three-rhombus-sums-in-a-grid
from typing import List

def getBiggestThree(grid: List[List[int]]) -> List[int]:
    m, n = len(grid), len(grid[0])
    sums = set()
    for r in range(m):
        for c in range(n):
            # A rhombus of size 0 consists of just one cell.
            sums.add(grid[r][c])
            # For a rhombus of size k > 0 with the top vertex at (r, c):
            # Right vertex → (r + k, c + k)
            # Bottom vertex → (r + 2k, c)
            # Left vertex → (r + k, c - k)

            k = 1
            # We can keep increasing the size of the rhombus until we go out of bounds.
            while r + 2 * k < m and c - k >= 0 and c + k < n:
                s = 0
                for t in range(k):
                    s += grid[r+t][c+t] 
                    s += grid[r+k+t][c+k-t] 
                    s += grid[r+2*k-t][c-t] 
                    s += grid[r+k-t][c-k+t]
                sums.add(s)
                k += 1
        return sorted(sums, reverse=True)[:3]
        
grid = [[1,2,3],[4,5,6],[7,8,9]]
print(getBiggestThree(grid))

grid = [[3,4,5,1,3],[3,3,4,2,3],[20,30,200,40,10],[1,5,5,4,1],[4,3,2,2,5]]
print(getBiggestThree(grid))

grid = [[7,7,7]]
print(getBiggestThree(grid))

grid = [[20,17,9,13,5,2,9,1,5],[14,9,9,9,16,18,3,4,12],[18,15,10,20,19,20,15,12,11],[19,16,19,18,8,13,15,14,11],[4,19,5,2,19,17,7,2,2]]
print(getBiggestThree(grid))

grid = [[4,5,3],[1,1,2],[1,3,4]]
print(getBiggestThree(grid))