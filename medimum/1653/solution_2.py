
# https://leetcode.com/problems/minimum-deletions-to-make-string-balanced

import emoji
def minimumDeletions(s: str) -> int:
    cost, b = 0, 0

    for  c in s:
        if c == 'b':
            b += 1
        elif c == 'a':
            cost = min(cost + 1, b)

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