# https://leetcode.com/problems/largest-submatrix-with-rearrangements

from git import List

def largestSubmatrix(matrix: List[List[int]]) -> int:
    m, n = len(matrix), len(matrix[0])
    prev_row = [0] * n

    max_area = 0
    for r in range(m):
        curr_row = matrix[r]
        for c in range(n):
            if curr_row[c] == 1:
                curr_row[c] += prev_row[c]

        sorted_row = sorted(curr_row, reverse=True)

        for c in range(n):
            max_area = max(max_area, sorted_row[c] * (c + 1))
            
        prev_row = curr_row
    return max_area


matrix = [[0,0,1],[1,1,1],[1,0,1]]

print(largestSubmatrix(matrix))

matrix = [[1,0,1,0,1]]

print(largestSubmatrix(matrix))

matrix = [[1,1,0],[1,0,1]]
print(largestSubmatrix(matrix))