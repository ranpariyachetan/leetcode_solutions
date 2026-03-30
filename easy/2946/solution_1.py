# https://leetcode.com/problems/matrix-similarity-after-cyclic-shifts

from typing import List
def areSimilar(mat: List[List[int]], k:int) -> bool:
    m = len(mat)
    n = len(mat[0])

    temp = [[0] * n for _ in range(m)]

    def shiftLeft(row):
        for c in range(k):
            x = row[0]
            for i in range(1, n):
                row[i - 1] = row[i]
            row[n - 1] = x
        return row
    def shiftRight(row):
        for c in range(k):
            x = row[n - 1]
            for i in range(n-2, -1, -1):
                row[i + 1] = row[i]
            row[0] = x
        return row
    for i in range(m):
        if i % 2 == 0:
            # shift k times to the left
            temp[i] = shiftLeft(mat[i][:])
        else:
            # shift k times to the right
            temp[i] = shiftRight(mat[i][:])
    return temp == mat

mat = [[1,2,3],[4,5,6],[7,8,9]]
k = 4

print(areSimilar(mat, k))