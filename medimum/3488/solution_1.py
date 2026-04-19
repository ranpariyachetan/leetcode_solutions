# https://leetcode.com/problems/closest-equal-element-queries


from git import List

# This is a brute force solution. 
# This solution is not efficient and will not pass all test cases on leetcode.
# The leetcode will time out on this solution.

def solveQueries(nums: List[int], queries: List[int]) -> List[int]:
    n = len(queries)
    m = len(nums)
    answer = [float("inf")] * n

    indices = {}

    for i, num in enumerate(nums):
        if not num in indices:
            indices[num] = []
        indices[num].append(i)

    for i, query in enumerate(queries):
        num = nums[query]
        if len(indices[num]) > 1:
            min_dist = answer[i]
            for j in indices[num]:
                if j != query:
                    min_dist = min(min_dist, min(abs(j - query), m - abs(j - query)))
            answer[i] = min_dist
        else:
            answer[i] = -1

    return answer


nums = [1,3,1,4,1,3,2]
queries = [0,3,5]

print(solveQueries(nums, queries))

nums = [1,2,3,4]
queries = [0,1,2,3]

print(solveQueries(nums, queries))

nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
queries = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]

print(solveQueries(nums, queries))