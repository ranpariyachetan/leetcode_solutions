
# Problem 744: Find Smallest Letter Greater Than Target
# https://leetcode.com/problems/find-smallest-letter-greater-than-target

def nextGreatestLetter(letters, target):
    n = len(letters)
    left = 0
    right = n - 1

    if target >= letters[-1]:
        return letters[0]
    
    while(left <= right):
        mid = (left + right) // 2
        if letters[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return letters[left]

letters = ["a","g", "i", "l", "m", "o", "p", "q", "q", "t", "w", "z"]
target = "q"

print(nextGreatestLetter(letters, target))