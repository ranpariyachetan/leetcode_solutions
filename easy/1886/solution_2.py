# https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation

# Solution using in-place rotation. Time complexity is O(n^2) and space complexity is O(1)
from typing import List

def findRotation(mat: List[List[int]], target: List[List[int]]) -> bool:
    n = len(mat)

    if mat == target:
        return True
    for _ in range(3):
        # In-place rotation of the matrix by 90 degrees in clockwise direction
        for i in range(n//2):
            c = n - 1 - i
            for j in range((n + 1) // 2):
                (mat[i][j], mat[j][c], mat[c][n - 1 - j], mat[n - 1 - j][i]) = (mat[n - 1 - j][i], mat[i][j], mat[j][c], mat[c][n - 1 - j])
        if mat == target:
            return True
    return False


mat = [[0,0,0],[0,1,0],[1,1,1]]
target = [[1,1,1],[0,1,0],[0,0,0]]
expected = True
actual = findRotation(mat, target)
print(f"Input = {mat}, Target = {target}, Expected = {expected}, Actual = {actual}")

mat = [[0,1],[1,1]]
target = [[1,0],[0,1]]
expected = False
actual = findRotation(mat, target)
print(f"Input = {mat}, Target = {target}, Expected = {expected}, Actual = {actual}")

mat = [[0,0,0],[0,1,0],[1,1,1]]
target = [[0,0,1],[0,1,1],[0,0,1]]
expected = True
actual = findRotation(mat, target)
print(f"Input = {mat}, Target = {target}, Expected = {expected}, Actual = {actual}")

mat = [[0,0,0],[0,0,1],[0,0,1]]
target = [[0,0,0],[0,0,1],[0,0,1]]
expected = True
actual = findRotation(mat, target)
print(f"Input = {mat}, Target = {target}, Expected = {expected}, Actual = {actual}")
