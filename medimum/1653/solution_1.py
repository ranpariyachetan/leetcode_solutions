
# https://leetcode.com/problems/minimum-deletions-to-make-string-balanced

import emoji
def minimumDeletions(s: str) -> int:
    cost = n = len(s)
    a_count, b_count = [0] * n, [0] * n
    a, b = 0, 0

    for i in range(n):
        b_count[i] = b
        if s[i] == 'b':
            b += 1

    for i in range(n -1, -1, -1):
        a_count[i] = a
        if s[i] == 'a':
            a += 1

    for i in range(n):
        cost = min(cost, b_count[i] + a_count[i])

    return cost



def print_test_result(input, expected, actual):
     print(f"{emoji.emojize(':check_mark_button:') if expected == actual else emoji.emojize(':cross_mark:')} Input = {input}, Expected = {expected}, Actual = {actual}")

input = "aababbab"
expected = 2
print_test_result(input, expected, minimumDeletions(input))
input = "bbaaaaabb"
expected = 2
print_test_result(input, expected, minimumDeletions(input))

input = "aaaaa"
expected = 0
print_test_result(input, expected, minimumDeletions(input))
input = "bbbbb"
expected = 0
print_test_result(input, expected, minimumDeletions(input))

input = "bbbbbbbaabbbbbaaabbbabbbbaabbbbbbaabbaaabaabbbaaaabaaababbbabbabbaaaabbbabbbbbaabbababbbaaaaaababaaababaabbabbbaaaabbbbbabbabaaaabbbaba"
expected = 60
print_test_result(input, expected, minimumDeletions(input))