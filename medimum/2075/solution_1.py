# https://leetcode.com/problems/decode-the-slanted-ciphertext

import emoji
def decodeCiphertext(encodedText: str, rows: int) -> str:
    n = len(encodedText)
    cols = n // rows
    result = []
    for i in range(cols):
        j = i
        while j < n:
            result.append(encodedText[j])
            j += cols + 1
    return "".join(result).rstrip()

def print_test_result(input, expected, actual):
    print(f"{emoji.emojize(':check_mark_button:') if expected == actual else emoji.emojize(':cross_mark:')} Input = {input}, Expected = {expected}, Actual = {actual}")

encodedText = "ch   ie   pr"
rows = 3
print_test_result((encodedText, rows), "cipher", decodeCiphertext(encodedText, rows))

encodedText = "iveo    eed   l te   olc"
rows = 4
print_test_result((encodedText, rows), "i love leetcode", decodeCiphertext(encodedText, rows))
