
# https://leetcode.com/problems/longest-common-suffix-queries

from typing import List

# This is a brute-force solution. We can optimize it using Trie data structure.
# This solution has a time complexity of O(n * m * k) where n is the number of words in wordsContainer, m is the number of words in wordsQuery and k is the average length of the words.
# The solution will not pass all the tests in Leecode due to time limit exceeded error.
def stringIndices(wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        n = len(wordsContainer)
        m = len(wordsQuery)
        ans = []
        
        shortest_idx = 0
        min_len = float('inf')
        for i, word in enumerate(wordsContainer):
            if len(word) < min_len:
                shortest_idx = i
                min_len = len(word)
        
        def findLongestSuffix(container, word) -> int:
            s_len = 0

            i = len(container) - 1
            j = len(word) - 1

            while i >=0 and j >=0 and container[i] == word[j]:
                i -= 1
                j -= 1
                s_len += 1

            return s_len

        for word in wordsQuery:
            suffix_len = 0
            idx = 0
            curr_word = ""
            for i, container in enumerate(wordsContainer):
                curr_len = findLongestSuffix(container, word)
                if curr_len > suffix_len:
                    suffix_len = curr_len
                    idx = i
                    curr_word = container
                elif curr_len == suffix_len:
                    if len(container) < len(curr_word):
                        idx = i
                        curr_word = container
            
            ans.append(idx if suffix_len > 0 else shortest_idx)

        return ans

wordsContainer = ["abcd","bcd","xbcd"]
wordsQuery = ["cd","bcd","xyz"]
print(stringIndices(wordsContainer, wordsQuery))