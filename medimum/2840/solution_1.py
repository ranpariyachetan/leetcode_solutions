# https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-ii

def checkStrings(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False

    odd_map1 = {}
    odd_map2 = {}
    even_map1 = {}
    even_map2 = {}
    for i in range(0, len(s1)):
        if i % 2 != 0:
            odd_map1[s1[i]] = odd_map1.get(s1[i], 0) + 1
            odd_map2[s2[i]] = odd_map2.get(s2[i], 0) + 1
        else:
            even_map1[s1[i]] = even_map1.get(s1[i], 0) + 1
            even_map2[s2[i]] = even_map2.get(s2[i], 0) + 1

    return odd_map1 == odd_map2 and even_map1 == even_map2

s1 = "abcdba"
s2 = "cabdab"

print(checkStrings(s1, s2))

s1 = "abe"
s2 = "bea"
print(checkStrings(s1, s2))