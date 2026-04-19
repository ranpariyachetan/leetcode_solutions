# https://leetcode.com/problems/minimum-distance-to-type-a-word-using-two-fingers

def minimumDistance(word: str) -> int:
    def dist(a: int, b: int) -> int:
        if a == -1 or b == -1:
            return 0

        ax, ay = a // 6, a % 6
        bx, by = b // 6, b % 6

        return abs(ax - bx) + abs(ay - by)

    n = len(word)
    dp = [[0] * 26 for _ in range(n)]

    for i in range(1, n):
        c = ord(word[i]) - ord('A')

        for j in range(26):
            dp[i][j] = min(dp[i - 1][j] + dist(c, ord(word[i - 1]) - ord('A')), dp[i - 1][c] + dist(j, ord(word[i - 1]) - ord('A')))

    return min(dp[-1])


word = "HAPPY"
print(minimumDistance(word))