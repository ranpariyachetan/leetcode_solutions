# https://leetcode.com/problems/maximum-distance-between-a-pair-of-values

from typing import List

def maxDistance(nums1: List[int], nums2: List[int]) -> int:
    answer = 0
    n = len(nums2)

    for i, num in enumerate(nums1):
        left, right = 0, n - 1

        while left <= right:
            mid = (left + right) // 2

            if num > nums2[mid]:
                right = mid - 1
            else:
                left = mid + 1

        if right >= i:
            answer = max(answer, right - i)

    return answer

nums1 = [55,30,5,4,2]
nums2 = [100,20,10,10,5]

print(maxDistance(nums1, nums2))

nums1 = [2,2,2]
nums2 = [10,10,1]
print(maxDistance(nums1, nums2))

nums1 = [30,29,19,5]
nums2 = [25,25,25,25,25]
print(maxDistance(nums1, nums2))