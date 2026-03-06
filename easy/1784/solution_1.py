# https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones

import emoji
def checkOnesSegment(s: str) -> bool:
    segments = 0
    flag = False
    for c in s:
        if c == "0":
            if flag:
                segments += 1
            flag = False
        else:
            flag = True

    if flag:
        segments += 1
    return segments == 1

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