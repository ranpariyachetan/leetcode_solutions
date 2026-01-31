
# Problem 744: Find Smallest Letter Greater Than Target
# https://leetcode.com/problems/find-smallest-letter-greater-than-target

def nextGreatestLetter(letters, target):
    letters = list(set(letters))
    letters.sort()
    for letter in letters:
        if letter > target:
            return letter
    return letters[0]


letters = ["a","g", "i", "l", "m", "o", "p", "q", "q", "t", "w", "z"]
target = "q"

print(nextGreatestLetter(letters, target))