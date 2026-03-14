# https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers

import emoji
def concatenatedBinary(n: int) -> int:
    result = 0
    mod = 10**9 + 7
    bits = 0

    for i in range(1, n + 1):
        if i & (i - 1) == 0:
            bits += 1
        result = ((result << bits) | i) % mod

    return result

def print_test_result(input, expected, actual):
     print(f"{emoji.emojize(':check_mark_button:') if expected == actual else emoji.emojize(':cross_mark:')} Input = {input}, Expected = {expected}, Actual = {actual}")

input = 1
expected = 1
print_test_result(input, expected, concatenatedBinary(input))

input = 3
expected = 27
print_test_result(input, expected, concatenatedBinary(input))

input = 12
expected = 505379714
print_test_result(input, expected, concatenatedBinary(input))