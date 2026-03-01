# https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers

import emoji

def minPartitions(n: str) -> int:
    return int(max(n))

def print_test_result(input, expected, actual):
     print(f"{emoji.emojize(':check_mark_button:') if expected == actual else emoji.emojize(':cross_mark:')} Input = {input}, Expected = {expected}, Actual = {actual}")


n = "32"
print_test_result(n, 3, minPartitions(n))

n = "82734"
print_test_result(n, 8, minPartitions(n))

n = "27346209830709182346"
print_test_result(n, 9, minPartitions(n))