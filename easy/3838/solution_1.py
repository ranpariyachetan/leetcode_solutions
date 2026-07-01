# https://leetcode.com/problems/weighted-word-mapping

from typing import List

def mapWordWeights(words: List[str], weights: List[int]) -> str:
    answer = ''
    for word in words:
        word_weight = sum(weights[ord(c) - ord('a')] for c in word)
        answer += (chr(ord('z') - (word_weight % 26)))
    return answer

words = ["abcd","def","xyz"]
weights = [5,3,12,14,1,2,3,2,10,6,6,9,7,8,7,10,8,9,6,9,9,8,3,7,7,2]

print(mapWordWeights(words, weights))

words = ["a","b","c"] 
weights = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
print(mapWordWeights(words, weights))

words = ["abcd"]
weights = [7,5,3,4,3,5,4,9,4,2,2,7,10,2,5,10,6,1,2,2,4,1,3,4,4,5]
print(mapWordWeights(words, weights))