# Divide an Array Into Subarrays With Minimum Cost I
# https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-i

from typing import List
def minimumCost(nums: List[int]) -> int:
        answer = float("inf")

        for i in range(1, len(nums) - 1):
            answer = min(answer, nums[0]+nums[i] + min(nums[i+1:]))

        return answer

nums = [1,15,7,9,2,5,10]

print("expected = 8")
print(f"actual = {minimumCost(nums)}")

nums = [3,7,1,12,4,11,8,2,6]
print("expected = 6")
print(f"actual = {minimumCost(nums)}")