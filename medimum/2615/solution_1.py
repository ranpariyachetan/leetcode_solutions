# https://leetcode.com/problems/sum-of-distances


from typing import List
def distance(nums: List[int]) -> List[int]:
    n = len(nums)
    answer = [0] * n
    
    idx_map = {}

    for i, num in enumerate(nums):
        if num in idx_map:
            idx_map[num].append(i)
        else:
            idx_map[num] = [i]

   
        for num, indices in idx_map.items():
            total = sum(indices)
            p_total = 0
            count = len(indices)

            for i, idx in enumerate(indices):
                answer[idx] = total - p_total * 2 + idx *(2 * i - count)
                p_total += idx
    return answer

nums = [1, 3, 1, 1, 2]
print(distance(nums))

nums = [2, 1, 4, 1, 1, 6, 7, 1]
print(distance(nums))