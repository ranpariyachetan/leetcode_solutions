# https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays
from typing import List
def findThePrefixCommonArray(A: List[int], B: List[int]) -> List[int]:
    n = len(A)
    countA = [0] * (n + 1)
    countB = [0] * (n + 1)
    result = []
    common_count = 0

    for i in range(n):
        countA[A[i]] += 1
        countB[B[i]] += 1

        if countA[A[i]] == 1 and countB[A[i]] == 1:
            common_count += 1
        if A[i] != B[i] and countA[B[i]] == 1 and countB[B[i]] == 1:
            common_count += 1

        result.append(common_count)

    return result


A = [1, 3, 2, 4]
B = [3, 1, 2, 4]
print(findThePrefixCommonArray(A, B))  # Output: [0, 2, 3, 4]

A = [2, 3, 1]
B = [3, 1, 2]
print(findThePrefixCommonArray(A, B))  # Output: [0, 1, 3]