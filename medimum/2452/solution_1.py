# https://leetcode.com/problems/words-within-two-edits-of-dictionary

from typing import List

def twoEditWords(queries: List[str], dictionary: List[str]) -> List[str]:

    def countEdits(word1: str, word2: str) -> bool:
        edits = 0
        for c1, c2, in zip(word1, word2):
            if c1 != c2:
                edits += 1
                if edits > 2:
                    return False
        return True
    
    result = []
    for query in queries:
        for word in dictionary:
            if len(query) != len(word):
                continue
            if countEdits(query, word):
                result.append(query)
                break
    return result

queries = ["word","note","ants","wood"]
dictionary = ["wood","joke","moat"]

print(twoEditWords(queries, dictionary))

queries = ["tsl","sri","yyy","rbc","dda","qus","hyb","ilu","ahd"]
dictionary = ["uyj","bug","dba","xbe","blu","wuo","tsf","tga"]

print(twoEditWords(queries, dictionary))