# https://leetcode.com/problems/count-the-number-of-special-characters-ii

def numberOfSpecialChars(word: str) -> int:
    lowercase = [-1] * 26
    uppercase = [-1] * 26

    result = 0

    for i in range(len(word)):
        ch = word[i]
        if ch.isupper():
            index = ord(ch) - ord('A')
            if uppercase[index] == -1:
                uppercase[index] = i
        else:
            index = ord(ch) - ord('a')
            lowercase[index] = i

    for i in range(26):
        if uppercase[i] != -1 and lowercase[i] != -1:
            if uppercase[i] > lowercase[i]:
                result += 1

    return result

word = "aaAbcBC"
print(numberOfSpecialChars(word))

word = "abc"
print(numberOfSpecialChars(word))

word = "AbBbCc"
print(numberOfSpecialChars(word))

word = "aaAaAbcBC"
print(numberOfSpecialChars(word))