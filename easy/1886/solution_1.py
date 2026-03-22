# https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation

# Solution using extra space to store the rotated matrix. Time complexity is O(n^2) and space complexity is O(n^2)
from typing import List

def findRotation(mat: List[List[int]], target: List[List[int]]) -> bool:
    n = len(mat)

    if mat == target:
        return True
    for _ in range(3):
        temp = [[0] * n for _ in range(n)]
        for i in range(n):
            c = n - 1 - i
            for j in range(n):
                temp[i][j] = mat[j][c]
        if temp == target:
            return True
        mat = temp

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
