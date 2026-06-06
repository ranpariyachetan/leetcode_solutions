# https://leetcode.com/problems/left-and-right-sum-differences

from typing import List

def leftRightDifference(nums: List[int]) -> List[int]:

    n = len(nums)
    leftSum, rightSum, answer = [0] * n, [0] * n, [0] * n

    for i in range(1, n):
        leftSum[i] = leftSum[i - 1] + nums[i - 1]
        rightSum[n - i - 1] = rightSum[n - i] + nums[n - i]

    for i in range(n):
        answer[i] = abs(leftSum[i] - rightSum[i])

    return answer

nums = [10, 4, 8 ,3]

print(leftRightDifference(nums))

nums = [1]
print(leftRightDifference(nums))