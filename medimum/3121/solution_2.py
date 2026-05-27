# https://leetcode.com/problems/count-the-number-of-special-characters-ii

def numberOfSpecialChars(word: str) -> int:
    lowercase = [-1] * 26
    uppercase = [-1] * 26

    result = {}

    for i in range(len(word)):
        ch = word[i]
        if ch.isupper():
            idx = ord(ch) - ord('A')
            if uppercase[idx] == -1:
                uppercase[idx] = i
            if lowercase[idx] != -1 and uppercase[idx] != -1:
                if uppercase[idx] > lowercase[idx]:
                    result[ch.lower()] = True
        else:
            idx = ord(ch) - ord('a')
            lowercase[idx] = i
            if lowercase[idx] != -1 and uppercase[idx] != -1:
                if uppercase[idx] < lowercase[idx]:
                    result[ch] = False

    return sum(1 for val in result.values() if val)

word = "aaAbcBC"
print(numberOfSpecialChars(word))

word = "abc"
print(numberOfSpecialChars(word))

word = "AbBbCc"
print(numberOfSpecialChars(word))

word = "aaAaAbcBC"
print(numberOfSpecialChars(word))

word = "dcbCC"
print(numberOfSpecialChars(word))