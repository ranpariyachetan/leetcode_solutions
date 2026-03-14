# https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n

import emoji
def getHappyString(n: int, k: int) -> str:
    letters = ["a", "b", "c"]

    # Total number of happy strings will be 3 * pow(2, n-1)
    if k > 3 * pow(2, n - 1):
        return ""

    happyStrings = []
    def createHappyString(prefix):
        if len(prefix) == n:
            happyStrings.append(prefix)
            return

        for ch in letters:
            if prefix == "" or prefix[-1] != ch:
                createHappyString(prefix + ch)

    createHappyString("")
    happyStrings = sorted(happyStrings)

    return happyStrings[k - 1]

def print_test_result(input, expected, actual):
     print(f"{emoji.emojize(':check_mark_button:') if expected == actual else emoji.emojize(':cross_mark:')} Input = {input}, Expected = {expected}, Actual = {actual}")

n = 1
k = 3
expected = "c"
print_test_result((n, k), expected, getHappyString(n, k))

n = 1
k = 4
expected = ""
print_test_result((n, k), expected, getHappyString(n, k))

n = 3
k = 9
expected = "cab"
print_test_result((n, k), expected, getHappyString(n, k))