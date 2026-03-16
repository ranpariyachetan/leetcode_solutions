# https://leetcode.com/problems/fancy-sequence

# this solution is not efficient and will not pass all test cases, but it is a working solution that can be optimized further. 
# The main idea is to keep track of the operations performed on the sequence and apply them when retrieving the value at a specific index.
class Fancy:

    def __init__(self):
        self.items = [] 
        self.signs = {}
        self.currIdx = -1
    def append(self, val: int) -> None:
        self.items.append(val)
        self.currIdx = len(self.items) - 1

    def addAll(self, inc: int) -> None:
        temp = self.signs.get(self.currIdx, [])
        temp.append(("+", inc))
        self.signs[self.currIdx] = temp

    def multAll(self, m: int) -> None:
        temp = self.signs.get(self.currIdx, [])
        temp.append(("*", m))
        self.signs[self.currIdx] = temp

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.items):
            return -1
        if idx > self.currIdx:
            return self.items[idx]

        output = self.items[idx]
        for k, sign in self.signs.items():
            if k >= idx:
                for s in sign:
                    if s[0] == "+":
                        output += s[1]
                    elif s[0] == "*":
                        output *= s[1]
                output = output % (10**9 + 7)
        return output


# # Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(2)
# obj.addAll(3)
# obj.append(7)
# obj.multAll(2)
# print(obj.getIndex(0) )
# obj.addAll(3)
# obj.append(10)
# obj.multAll(2)
# print(obj.getIndex(0))
# print(obj.getIndex(1))
# print(obj.getIndex(2))

obj = Fancy()
obj.addAll(3)
obj.getIndex(0)
# param_4 = obj.getIndex(idx)

# print(param_4)