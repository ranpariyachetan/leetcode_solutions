# https://leetcode.com/problems/search-in-rotated-sorted-array/

from typing import List

def search(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left < right and  nums[left] < nums[left + 1]:
       left += 1

    x1, y1 = 0, left
    x2, y2 = left + 1, right

    if target >= nums[x1] and target <= nums[y1]:
        left, right = x1, y1
    else:        
        left, right = x2, y2

    while left <= right:
        middle = left + (right - left) // 2

        if nums[middle] == target:
            return middle
        elif nums[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return -1


input = [4,5,6,7,0,1,2]
target = 0

print(search(input, target))

input = [4,5,6,7,0,1,2]
target = 3
print(search(input, target))

input = [1]
target = 0
print(search(input, target))