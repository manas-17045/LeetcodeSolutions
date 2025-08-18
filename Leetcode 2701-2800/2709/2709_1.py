# Leetcode 2709: Greatest Common Divisor Traversal
# https://leetcode.com/problems/greatest-common-divisor-traversal/
# Solved on 18th of August, 2025
class Solution:
    def canTraverseAllPairs(self, nums: list[int]) -> bool:
        """
        Determines if all pairs of numbers in the input list can be traversed.

        Args:
            nums (list[int]): A list of integers.
        Returns:
            bool: True if all pairs can be traversed, False otherwise.
        """
        class DSU:
            def __init__(self, count: int):
                self.parent = list(range(count))
                self.size = [1] * count

            def find(self, i: int) -> int:
                if self.parent[i] == i:
                    return i
                self.parent[i] = self.find(self.parent[i])
                return self.parent[i]

            def union(self, i: int, j: int) -> bool:
                rootI = self.find(i)
                rootJ = self.find(j)
                if rootI != rootJ:
                    if self.size[rootI] < self.size[rootJ]:
                        rootI, rootJ = rootJ, rootI
                    self.parent[rootJ] = rootI
                    self.size[rootI] += self.size[rootJ]
                    return True
                return False

        numCount = len(nums)
        if numCount <= 1:
            return True

        uniqueNums = set(nums)
        if 1 in uniqueNums:
            return False

        maxNum = max(uniqueNums)

        spf = list(range(maxNum + 1))
        i = 2
        while i * i <= maxNum:
            if spf[i] == i:
                for j in range(i * i, maxNum + 1, i):
                    if spf[j] == j:
                        spf[j] = i
            i += 1

        dsu = DSU(maxNum + 1)

        for num in uniqueNums:
            tempNum = num
            while tempNum > 1:
                primeFactor = spf[tempNum]
                dsu.union(num, primeFactor)
                while tempNum % primeFactor == 0:
                    tempNum //= primeFactor

        firstNumRoot = dsu.find(nums[0])
        for i in range(1, numCount):
            if dsu.find(nums[i]) != firstNumRoot:
                return False

        return True