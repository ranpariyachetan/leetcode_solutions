# https://leetcode.com/problems/find-the-string-with-lcp

from typing import List

def findTheString(lcp: List[List[int]]) -> str:
    n = len(lcp)
    ans = [''] * n

    ch = ord('a')
    for i in range(n):
        if ans[i]:
            continue

        if ch > ord('z'):
            return ""
        
        for j in range(i, n):
            if lcp[i][j] > 0:
                ans[j] = chr(ch)
        ch += 1
        
    word = ''.join(ans)

    print(f"word: {word}")

    if len(word) != n:
            return ""
    
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(n - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if word[i] == word[j]:
                dp[i][j] = 1 + dp[i + 1][j + 1]
        
    for i in range(n):
        for j in range(n):
            if dp[i][j] != lcp[i][j]:
                return ""
            
    return word

lcp = [[4,0,2,0],[0,3,0,1],[2,0,2,0],[0,1,0,1]]

print(findTheString(lcp))

lcp = [[4,3,2,1],[3,3,2,1],[2,2,2,1],[1,1,1,1]]
print(findTheString(lcp))

# lcp = [[0]]
# print(findTheString(lcp))

lcp = [[1, 0], [0, 0]]
print(findTheString(lcp))