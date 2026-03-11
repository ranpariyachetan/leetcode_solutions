# https://leetcode.com/problems/complement-of-base-10-integer

import emoji
def bitwiseComplement(n: int) -> int:
    if n == 0:
        return 1

    result, bit = 0, 1

    while n > 0:
        if (n & 1) == 0:
            result += bit
        n >>= 1
        bit <<= 1

    return result


def print_test_result(input, expected, actual):
     print(f"{emoji.emojize(':check_mark_button:') if expected == actual else emoji.emojize(':cross_mark:')} Input = {input}, Expected = {expected}, Actual = {actual}")


input = 5
expected = 2
print_test_result(input, expected, bitwiseComplement(input))

input = 7
expected = 0
print_test_result(input, expected, bitwiseComplement(input))

input = 10
expected = 5
print_test_result(input, expected, bitwiseComplement(input))