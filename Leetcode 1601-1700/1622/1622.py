# Leetcode 1622: Fancy Sequence
# https://leetcode.com/problems/fancy-sequence/
# Solved on 15th of March, 2026
class Fancy:

    def __init__(self):
        self.sequenceList = []
        self.addFactor = 0
        self.multFactor = 1
        self.modValue = 1000000007

    def append(self, val: int) -> None:
        normalizedVal = (val - self.addFactor) % self.modValue
        invMult = pow(self.multFactor, self.modValue - 2, self.modValue)
        finalVal = (normalizedVal * invMult) % self.modValue
        self.sequenceList.append(finalVal)

    def addAll(self, inc: int) -> None:
        self.addFactor = (self.addFactor + inc) % self.modValue

    def multAll(self, m: int) -> None:
        self.multFactor = (self.multFactor * m) % self.modValue
        self.addFactor = (self.addFactor * m) % self.modValue

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.sequenceList):
            return -1

        return (self.sequenceList[idx] * self.multFactor + self.addFactor) % self.modValue