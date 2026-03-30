# https://leetcode.com/problems/matrix-similarity-after-cyclic-shifts

from typing import List
def areSimilar(mat: List[List[int]], k:int) -> bool:
    m = len(mat)
    n = len(mat[0])
    k %= n

    for i in range(m):
        for j in range(n):
            if mat[i][j] != mat[i][(j + k) % n]:
                return False
    return True


mat = [[1,2,3],[4,5,6],[7,8,9]]
k = 4

print(areSimilar(mat, k))