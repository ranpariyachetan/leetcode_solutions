# https://leetcode.com/problems/jump-game-vii

from typing import List
from collections import deque

def canReach(s: str, minJump: int, maxJump: int) -> bool:
    n = len(s)
    if s[-1] != '0':
        return False

    queue = deque([0])
    farthest = 0

    while queue:
        i = queue.popleft()

        start = max(i + minJump, farthest + 1)
        end = min(i + maxJump + 1, n)

        for j in range(start, end):
            if s[j] == '0':
                if j == n - 1:
                    return True
                queue.append(j)

        farthest = max(farthest, end - 1)

    return False

s = "011010"
minJump = 2
maxJump = 3
print(canReach(s, minJump, maxJump))  # Output: True

s = "01101110"
minJump = 2
maxJump = 3
print(canReach(s, minJump, maxJump))  # Output: False

s = "0000000000"
minJump = 2
maxJump = 5
print(canReach(s, minJump, maxJump))  # Output: True