# https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating

# Brute force solution. Time limit exceeded.
import emoji

def minFlips(s: str) -> int:
    l = len(s)

    output1 = ''.join(str(i % 2) for i in range(l))

    output2 = ''.join(str((i + 1) % 2) for i in range(l))

    ans1 = 0
    ans2 = 0
    ans = float('inf')
    for i in range(0, l):
        temps = s[i:] + s[:i]
        ans1 = 0
        ans2 = 0
        for j in range(l):
            if temps[j] != output1[j]:
                ans1 += 1
            if temps[j] != output2[j]:
                ans2 += 1
        ans = min(ans, min (ans1, ans2))
    
    return ans

def print_test_result(input, expected, actual):
     print(f"{emoji.emojize(':check_mark_button:') if expected == actual else emoji.emojize(':cross_mark:')} Input = {input}, Expected = {expected}, Actual = {actual}")

input = "111000"
expected = 2
print_test_result(input, expected, minFlips(input))

input = "010"
expected = 0
print_test_result(input, expected, minFlips(input))

input = "1110"
expected = 1
print_test_result(input, expected, minFlips(input))

input = "01001001101"
expected = 2
print_test_result(input, expected, minFlips(input))