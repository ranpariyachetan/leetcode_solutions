# https://leetcode.com/problems/check-if-array-is-sorted-and-rotated

from typing import List
def check(nums: List[int]) -> bool:
    n = len(nums)
    for x in range(n):
        temp = [0] * n
        for i in range(n):
            temp[i] = nums[(i + x) % n]
            if i > 0 and temp[i] < temp[i - 1]:
                break
        else:
            return True

    return False


input = [3,4,5,1,2]
print(check(input))
input = [2,1,3,4]
print(check(input))
input = [1,2,3]
print(check(input))
nums = [2,1]
print(check(nums))