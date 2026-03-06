# https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones

import emoji
def checkOnesSegment(s: str) -> bool:
    return "01" not in s

def print_test_result(input, expected, actual):
     print(f"{emoji.emojize(':check_mark_button:') if expected == actual else emoji.emojize(':cross_mark:')} Input = {input}, Expected = {expected}, Actual = {actual}")


input = "1001"
expected = False
print_test_result(input, expected, checkOnesSegment(input))

input = "110"
expected = True
print_test_result(input, expected, checkOnesSegment(input))

input = "101"
expected = False
print_test_result(input, expected, checkOnesSegment(input))

input = "1101111"
expected = False
print_test_result(input, expected, checkOnesSegment(input))