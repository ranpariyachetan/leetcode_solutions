# https://leetcode.com/problems/maximum-amount-of-money-robot-can-earn

from typing import List
import emoji

def maximumAmount(coins: List[List[int]]) -> int:
    m = len(coins)
    n = len(coins[0])
    k = 3
    dp = [[[-10**9] * k for _ in range(n)] for _ in range(m)]
    dp[0][0][1] = dp[0][0][2] = 0
    dp[0][0][0] = coins[0][0]
    
    for i in range(m):
        for j in range(n):
            for l in range(k):
                if i > 0:
                    dp[i][j][l] = max(dp[i][j][l], dp[i-1][j][l] + coins[i][j])
                if i > 0 and l > 0:
                    dp[i][j][l] = max(dp[i][j][l], dp[i-1][j][l-1])
                if j > 0:
                    dp[i][j][l] = max(dp[i][j][l], dp[i][j-1][l] + coins[i][j])
                if j > 0 and l > 0:
                    dp[i][j][l] = max(dp[i][j][l], dp[i][j-1][l-1])

    return max(dp[m-1][n-1])

def print_test_result(input, expected, actual):
    print(f"{emoji.emojize(':check_mark_button:') if expected == actual else emoji.emojize(':cross_mark:')} Input = {input}, Expected = {expected}, Actual = {actual}")

coins = [[0, 1, -1],[1,-2,3],[2,-3,4]]
expected = 8
print_test_result(coins, expected, maximumAmount(coins))

coins = [[-4]]
expected = 0
print_test_result(coins, expected, maximumAmount(coins))

coins = [[-7,12,12,13],[-6,19,19,-6],[9,-2,-10,16],[-4,14,-10,-9]]
expected = 60
print_test_result(coins, expected, maximumAmount(coins))