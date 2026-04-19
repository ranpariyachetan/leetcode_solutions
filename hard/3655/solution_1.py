# https://leetcode.com/problems/xor-after-range-multiplication-queries-ii

from typing import List
from math import isqrt

def xorAfterQueries(nums: List[int], queries: List[List[int]]) -> int:
    MOD = 10 ** 9 + 7
    n = len(nums)
    B = isqrt(n) + 1

    mul = [1] * n

    diff = {}

    def modinv(x: int) -> int:
        return pow(x, MOD - 2, MOD)
    
    for l, r, k, v in queries:
        if k > B:
            for i in range(l, r + 1, k):
                mul[i] = (mul[i] * v) % MOD
        else:
            rem = l % k
            key = (k, rem)

            # length of this residue-class sequence
            m = (n - 1 - rem) // k + 1

            if key not in diff:
                diff[key] = [1] * (m + 1)

            arr = diff[key]

            start = (l - rem) // k
            end = (r - rem) // k

            arr[start] = (arr[start] * v) % MOD
            if end + 1 < len(arr):
                arr[end + 1] = (arr[end + 1] * modinv(v)) % MOD

    for (k, rem), arr in diff.items():
            cur = 1
            idx = rem
            for t in range(len(arr) - 1):
                cur = (cur * arr[t]) % MOD
                mul[idx] = (mul[idx] * cur) % MOD
                idx += k


    ans = 0
    for i in range(n):
        val = (nums[i] * mul[i]) % MOD
        ans ^= val

    return ans


nums = [1,1,1]
queries = [[0,2,1,4]]
print(xorAfterQueries(nums, queries))

nums = [2,3,1,5,4]
queries = [[1,4,2,3],[0,2,1,2]]

print(xorAfterQueries(nums, queries))
