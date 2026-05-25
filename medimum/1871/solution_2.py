# https://leetcode.com/problems/jump-game-vii

from typing import List

def canReach(s: str, minJump: int, maxJump: int) -> bool:
    n = len(s)
    if s[-1] != '0' or s[0] != '0':
        return False

    reachable = [False] * n
    reachable[0] = True
    count = 0

    for i in range(1, n):
        if i - minJump >= 0 and reachable[i - minJump]:
            count += 1

        if i - maxJump - 1 >= 0 and reachable[i - maxJump - 1]:
            count -= 1

        if count > 0 and s[i] == '0':
            reachable[i] = True

    return reachable[n - 1]

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