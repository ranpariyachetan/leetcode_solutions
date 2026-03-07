# https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating

import emoji

def minFlips(s: str) -> int:
    l = len(s)

    output1 = ''.join(str(i % 2) for i in range(2*l))

    output2 = ''.join(str((i + 1) % 2) for i in range(2*l))

    ans1 = 0
    ans2 = 0
    ans = float('inf')
    n = 0
    temp = s + s
    for i in range(2*l):
        if temp[i] != output1[i]:
            ans1 += 1
        if temp[i] != output2[i]:
            ans2 += 1

        if i - n + 1 > l:
            if temp[n] != output1[n]:
                ans1 -= 1
            if temp[n] != output2[n]:
                ans2 -= 1
            n += 1
        if i - n + 1 == l:
            ans = min(ans, min (ans1, ans2))
    
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