# Leetcode 4054: Count Shadow Pairs I
# https://leetcode.com/problems/count-shadow-pairs-i/
# Solved on 19th of October, 2026
class Solution:
    def shadowPairs(self, nums: list[int]) -> int:
        """
        Calculates the total number of shadow pairs in the array.

        Parameters:
            nums (list[int]): Array of integers.

        Returns:
            int: Total number of shadow pairs.
        """
        totalPairs = 0
        aliveCount = 0
        monoStack = []

        for currentValue in nums:
            while monoStack and monoStack[-1][0] > currentValue:
                poppedValue, poppedCount = monoStack.pop()
                aliveCount -= poppedCount

            equalCount = 0
            if monoStack and monoStack[-1][0] == currentValue:
                equalCount = monoStack[-1][1]

            totalPairs += aliveCount - equalCount

            if monoStack and monoStack[-1][0] == currentValue:
                monoStack[-1][1] += 1
            else:
                monoStack.append([currentValue, 1])

            aliveCount += 1

        return totalPairs