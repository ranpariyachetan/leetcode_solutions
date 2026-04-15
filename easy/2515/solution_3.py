
# https://leetcode.com/problems/shortest-distance-to-target-string-in-a-circular-array

from git import List
from math import inf

def closestTarget(words: List[str], target: str, startIndex: int) -> int:
    n = len(words)
    i, answer = startIndex, inf

    if words[startIndex] == target:
        return 0

    i = (i + 1) % n    
    while i != startIndex:
        if words[i] == target:
            answer = min(answer, min(abs(i - startIndex), n - abs(i - startIndex)))
        i = (i + 1) % n

    return  -1 if answer == inf else answer

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