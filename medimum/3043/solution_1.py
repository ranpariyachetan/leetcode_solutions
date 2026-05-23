# https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix

from typing import List
def longestCommonPrefix(arr1: List[int], arr2: List[int]) -> int:
    m, n = len(arr1), len(arr2)

    prefixes = set()

    for num in arr1:
        prefixes.add(num)
        while num > 0:
            num = num // 10
            prefixes.add(num)

    prefix = 0
    for num in arr2:
        if num in prefixes:
            prefix = max(prefix, num)
        while num > 0:
            num = num // 10
            if num in prefixes:
                prefix = max(prefix, num)

    count = 0
    while prefix > 0:
        count += 1
        prefix = prefix // 10
    return count

arr1 = [1, 10, 100]
arr2 = [1000]

print(longestCommonPrefix(arr1, arr2))  # Output: 3

arr1 = [1,2,3]
arr2 = [4,4,4]
print(longestCommonPrefix(arr1, arr2))  # Output: 0