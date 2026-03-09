# https://leetcode.com/problems/find-unique-binary-string
import emoji

def findDifferentBinaryString(nums: list[str]) -> str:
    l = len(nums)

    ans = ["0"] * l
    for i in range(l):
        if nums[i][i] == '0':
            ans[i] = '1'
    return "".join(ans)

def print_test_result(input, expected, actual):
     print(f"{emoji.emojize(':check_mark_button:') if actual in expected else emoji.emojize(':cross_mark:')} Input = {input}, Expected = {expected}, Actual = {actual}")

input = ["01","10"]
expected = ["00", "11"]
print_test_result(input, expected, findDifferentBinaryString(input))

input = ["00","01"]
expected = ["11","10"]
print_test_result(input, expected, findDifferentBinaryString(input))

input = ["111","011","001"]
expected = ["000", "010", "100", "110"]
print_test_result(input, expected, findDifferentBinaryString(input))