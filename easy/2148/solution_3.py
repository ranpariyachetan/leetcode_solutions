# Problem 2148: Count Elements With Strictly Smaller and Greater Elements
# https://leetcode.com/problems/count-elements-with-strictly-smaller-and-greater-elements

from typing import List
def countElements(nums: List[int]) -> int:
    min_num = min(nums)
    max_num = max(nums)

    answer = 0
    for num in nums:
        if num != min_num and num != max_num:
            answer += 1
    return answer

nums = [-1,-1,-1,0,0,0]
print(countElements(nums))

nums = [3,692,193,93,192,4,2,60,23,193,593,293,283,83,295,30,985,48,472,274,472,74]
print(countElements(nums))

nums = [11,11,11,11]
print(countElements(nums))

nums = [-3,3,3,90]
print(countElements(nums))

nums = [11,7,2,15]
print(countElements(nums))