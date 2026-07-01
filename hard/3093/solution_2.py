
# https://leetcode.com/problems/longest-common-suffix-queries

from typing import List
class TrieNode:
    def __init__(self):
        self.children = {}
        self.index = float('inf')
        self.min_length = float('inf')
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str, index: int):
        node = self.root

        if len(word) < node.min_length:
            node.min_length = len(word)
            node.index = index

        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]

            if len(word) < node.min_length:
                node.min_length = len(word)
                node.index = index
    
    def search(self, word: str) -> int:
        node = self.root
        for ch in word:
            if ch in node.children:
                node = node.children[ch]
            else:
                break
        return node.index
def stringIndices(wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        ans = []
        
        trie = Trie()
        for i, word in enumerate(wordsContainer):
            rev_word = word[::-1]
            trie.insert(rev_word, i)

        for word in wordsQuery:
            rev_word = word[::-1]
            ans.append(trie.search(rev_word))

        return ans

wordsContainer = ["abcd","bcd","xbcd"]
wordsQuery = ["cd","bcd","xyz"]
print(stringIndices(wordsContainer, wordsQuery))

wordsContainer = ["abcdefgh","poiuygh","ghghgh"]
wordsQuery = ["gh","acbfgh","acbfegh"]
print(stringIndices(wordsContainer, wordsQuery))