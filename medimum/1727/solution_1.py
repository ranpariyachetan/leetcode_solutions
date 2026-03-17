# https://leetcode.com/problems/largest-submatrix-with-rearrangements

from git import List

def largestSubmatrix(matrix: List[List[int]]) -> int:
    m, n = len(matrix), len(matrix[0])
    for r in range(1, m):
        for c in range(n):
            if matrix[r][c] == 1:
                matrix[r][c] += matrix[r-1][c]

    max_area = 0
    for r in range(m):
        sorted_row = sorted(matrix[r], reverse=True)
        for c in range(n):
            max_area = max(max_area, sorted_row[c] * (c + 1))

    return max_area


matrix = [[0,0,1],[1,1,1],[1,0,1]]

print(largestSubmatrix(matrix))

matrix = [[1,0,1,0,1]]

print(largestSubmatrix(matrix))

matrix = [[1,1,0],[1,0,1]]
print(largestSubmatrix(matrix))