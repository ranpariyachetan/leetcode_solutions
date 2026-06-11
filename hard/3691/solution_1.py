# https://leetcode.com/problems/maximum-total-subarray-value-ii

from typing import List
from heapq import heappush, heappop, heapify


def maxTotalValue(nums: List[int], k: int) -> int:
    n = len(nums)

    levels = n.bit_length()
    hi = [nums[:]]
    lo = [nums[:]]

    for j in range(1, levels):
        half = 1 << (j - 1)
        prev_hi, prev_lo = hi[j - 1], lo[j - 1]
        hi.append([max(prev_hi[i], prev_hi[i + half]) for i in range(n - (1 << j) + 1)])
        lo.append([min(prev_lo[i], prev_lo[i + half]) for i in range(n - (1 << j) + 1)])

    log2 = [0] * (n + 1)
    for i in range(2, n + 1):
        log2[i] = log2[i >> 1] + 1

    def val(l: int, r: int) -> int:
        t = log2[r - l + 1]
        return max(hi[t][l], hi[t][r - (1 << t) + 1]) - min(lo[t][l], lo[t][r - (1 << t) + 1])

    heap = [(-val(l, n - 1), l, n - 1) for l in range(n)]
    heapify(heap)

    ans = 0
    for _ in range(k):
        neg_v, l, r = heappop(heap)
        ans -= neg_v
        if r > l:
            heappush(heap, (-val(l, r - 1), l, r - 1))

    return ans
