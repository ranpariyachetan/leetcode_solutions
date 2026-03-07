# https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating

import emoji

def minFlips(s: str) -> int:
    l = len(s)
    ans = l

    op = [0, 0]
    for i in range(l):
        op[(ord(s[i])^i)&1] += 1

    for i in range(l):
        c = ord(s[i])
        op[(c ^ i) & 1] -= 1
        op[(c ^ (l + i)) & 1] += 1
        ans = min(ans, min(op))
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