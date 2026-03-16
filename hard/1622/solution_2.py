# https://leetcode.com/problems/fancy-sequence

class Fancy:

    def __init__(self):
        self.items = []
        self.add = 0
        self.mult = 1
        self.MOD = 10**9 + 7

    def modInverse(self, a):
        return pow(a, self.MOD - 2, self.MOD)
    
    def append(self, val: int) -> None:
        self.items.append((val - self.add) * self.modInverse(self.mult) % self.MOD)

    def addAll(self, inc: int) -> None:
        self.add = (self.add + inc) % self.MOD

    def multAll(self, m: int) -> None:
        self.add = (self.add * m) % self.MOD
        self.mult = (self.mult * m) % self.MOD
        
    def getIndex(self, idx: int) -> int:
        if idx >= len(self.items):
            return -1
        
        return (self.items[idx] * self.mult + self.add) % self.MOD

# # Your Fancy object will be instantiated and called as such:
obj = Fancy()
obj.append(2)
obj.addAll(3)
obj.append(7)
obj.multAll(2)
print(obj.getIndex(0) )
obj.addAll(3)
obj.append(10)
obj.multAll(2)
print(obj.getIndex(0))
print(obj.getIndex(1))
print(obj.getIndex(2))

obj = Fancy()
obj.addAll(3)
print(obj.getIndex(0))
# param_4 = obj.getIndex(idx)

# print(param_4)