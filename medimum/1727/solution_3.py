# https://leetcode.com/problems/largest-submatrix-with-rearrangements

from git import List

def largestSubmatrix(matrix: List[List[int]]) -> int:
    m, n = len(matrix), len(matrix[0])
    prev_heigths = []
    max_area = 0

    for r in range(m):
        heights = []
        seen = [False] * n

        for height, c in prev_heigths:
            if matrix[r][c]==1:
                heights.append((height + 1, c))
                seen[c] = True

        for c in range(n):
            if matrix[r][c] == 1 and not seen[c]:
                heights.append((1, c))
    
        for i in range(len(heights)):
            height, c = heights[i]
            max_area = max(max_area, height * (i + 1))

        prev_heigths = heights
        
    return max_area


matrix = [[0,0,1],[1,1,1],[1,0,1]]

print(largestSubmatrix(matrix))

matrix = [[1,0,1,0,1]]

print(largestSubmatrix(matrix))

matrix = [[1,1,0],[1,0,1]]
print(largestSubmatrix(matrix))