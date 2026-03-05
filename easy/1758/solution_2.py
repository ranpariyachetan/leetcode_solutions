# https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string

import emoji

def minOperations(s: str) -> int:
    l = len(s)

    start0 = 0
    start1 = 0
    
    for i in range(l):
         if i % 2 == 0:
             if s[i] != '0':
                 start0 += 1
             if s[i] != '1':
                 start1 += 1
         else:
             if s[i] != '1':
                 start0 += 1
             if s[i] != '0':
                 start1 += 1

    return min (start0, start1)

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