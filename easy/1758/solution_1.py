# https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string

import emoji

def minOperations(s: str) -> int:
    l = len(s)

    ones = [1] * (l//2)
    zeros = [0] * (l//2)

    output1 = ''.join(str(i % 2) for i in range(l))

    output2 = ''.join(str((i + 1) % 2) for i in range(l))

    ans1 = 0
    ans2 = 0

    for i in range(l):
        if s[i] != output1[i]:
            ans1 += 1
        if s[i] != output2[i]:
            ans2 += 1

    return min (ans1, ans2)

def print_test_result(input, expected, actual):
     print(f"{emoji.emojize(':check_mark_button:') if expected == actual else emoji.emojize(':cross_mark:')} Input = {input}, Expected = {expected}, Actual = {actual}")

input = "0100"
expected = 1
print_test_result(input, expected, minOperations(input))

input = "10"
expected = 0
print_test_result(input, expected, minOperations(input))

input = "1111"
expected = 2
print_test_result(input, expected, minOperations(input))