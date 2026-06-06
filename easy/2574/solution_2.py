# https://leetcode.com/problems/left-and-right-sum-differences

from typing import List

def leftRightDifference(nums: List[int]) -> List[int]:

    n = len(nums)
    leftSum, rightSum, answer = 0, 0, [0] * n

    for i in range(0, n):
        answer[i] = leftSum
        leftSum += nums[i]

    for i in range(n - 1, -1, -1):
        answer[i] = abs(answer[i] - rightSum)
        rightSum += nums[i]

    return answer

nums = [10, 4, 8 ,3]

print(leftRightDifference(nums))

nums = [1]
print(leftRightDifference(nums))