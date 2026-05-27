# https://leetcode.com/problems/count-the-number-of-special-characters-i

def numberOfSpecialChars(word: str) -> int:
    lowercase = {}
    uppercase = {}

    result = set()
    for ch in word:
        if ch.isupper():
            uppercase[ch] = True
            if ch.lower() in lowercase:
                result.add(ch.lower())
        else:
            lowercase[ch] = True
            if ch.upper() in uppercase:
                result.add(ch)
    return len(result)

word = "aaAbcBC"
print(numberOfSpecialChars(word))

word = "abBCab"
print(numberOfSpecialChars(word))