# https://leetcode.com/problems/maximum-distance-between-a-pair-of-values

from typing import List

def maxDistance(nums1: List[int], nums2: List[int]) -> int:
    answer = 0
    
    # Let's use two pointers to traverse both arrays
    i, j = 0, 0
    n, m = len(nums1), len(nums2)
    while i < n and j < m:
        if nums1[i] <= nums2[j]:
            # If the current element in nums1 is less than or equal to the current element in nums2,
            # we can calculate the distance and move the pointer in nums2 to find a potentially larger distance
            answer = max(answer, j - i)
            j += 1
        else:
            # If the current element in nums1 is greater than the current element in nums2,
            # we need to move the pointer in nums1 to find a smaller element that can be paired with the current element in nums2
            i += 1
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