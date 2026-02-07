
# https://leetcode.com/problems/transformed-array

from typing import List
def constructTransformedArray(nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n

        for i in range(n):
            result[i] = nums[(i + nums[i]) % n]

        return result

input = [3,-2,1,1]
print(constructTransformedArray(input))  # expected = [1,1,1,3]

input = [-1,4,-1]
print(constructTransformedArray(input))  # expected = [-1,-1,4]