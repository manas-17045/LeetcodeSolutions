# Leetcode 3669: Balanced K-Factor Decomposition
# https://leetcode.com/problems/balanced-k-factor-decomposition/
# Solved on 28th of December, 2025
class Solution:
    def minDifference(self, n: int, k: int) -> list[int]:
        """
        Finds a k-factor decomposition of n such that the difference between the maximum and minimum factors is minimized.

        :param n: The number to decompose.
        :param k: The number of factors.
        :return: A list of k factors that minimize the difference between the maximum and minimum factors.
        """
        self.minDiff = float('inf')
        self.bestSplit = []

        def findSplit(currentN, kLeft, minVal, currentPath):
            if self.minDiff == 0:
                return

            if kLeft == 1:
                if currentN >= minVal:
                    diff = currentN - currentPath[0]
                    if diff < self.minDiff:
                        self.minDiff = diff
                        self.bestSplit = currentPath + [currentN]
                return

            factor = minVal
            while factor ** kLeft <= currentN:
                if currentN % factor == 0:
                    findSplit(currentN // factor, kLeft - 1, factor, currentPath + [factor])
                factor += 1

        findSplit(n, k, 1, [])
        return self.bestSplit