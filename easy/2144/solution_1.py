# https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount

from typing import List
def minimumCost(cost: List[int]) -> int:
    cost.sort(reverse=True)
    i = 0
    idx = i + (i // 2)

    answer = 0

    while idx < len(cost):
        answer += cost[idx]
        i += 1
        idx = i + (i // 2)

    return answer

cost = [1, 2, 3]
print(minimumCost(cost))

cost = [6,5,7,9,2,2]
print(minimumCost(cost))