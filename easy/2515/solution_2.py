
# https://leetcode.com/problems/shortest-distance-to-target-string-in-a-circular-array

from git import List
from math import inf

def closestTarget(words: List[str], target: str, startIndex: int) -> int:
    n = len(words)

    return  -1 if (answer := min((min(abs((startIndex + k) % n - startIndex), n - abs((startIndex + k) % n - startIndex)) for k in range(n) if words[(startIndex + k) % n] == target), default=inf)) == inf else answer

words = ["hello","i","am","leetcode","hello"]
target = "hello"
startIndex = 1
print(closestTarget(words, target, startIndex))

words = ["a","b","leetcode"]
target = "leetcode"
startIndex = 0
print(closestTarget(words, target, startIndex))

word = ["i","eat","leetcode"]
target = "ate"
startIndex = 0
print(closestTarget(word, target, startIndex))