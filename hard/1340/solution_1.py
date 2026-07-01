# https://leetcode.com/problems/jump-game-v/

from typing import List
def maxJumps(arr: List[int], d: int) -> int:
    memo = {}

    def dfs(i):
        if i in memo:
            return memo[i]

        max_jumps = 1

        # Try jumping left within distance d
        j = i - 1
        while j >= 0 and i - j <= d and arr[j] < arr[i]:
            max_jumps = max(max_jumps, 1 + dfs(j))
            j -= 1

        # Try jumping right within distance d
        j = i + 1
        while j < len(arr) and j - i <= d and arr[j] < arr[i]:
            max_jumps = max(max_jumps, 1 + dfs(j))
            j += 1

        memo[i] = max_jumps
        return max_jumps

    return max(dfs(i) for i in range(len(arr)))

arr = [6,4,14,6,8,13,9,7,10,6,12]
d = 2
print(maxJumps(arr, d))  # Output: 4

arr = [3,3,3,3,3]
d = 3
print(maxJumps(arr, d))  # Output: 1

arr = [7,6,5,4,3,2,1]
d = 1
print(maxJumps(arr, d))  # Output: 7