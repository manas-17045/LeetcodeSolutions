# Leetcode 4010: Maximize Pair Strength Using GCD
# https://leetcode.com/problems/maximize-pair-strength-using-gcd/
# Solved on 2nd of September, 2026
from math import gcd


class Solution:
    def maxPairStrength(self, nums: list[int]) -> int:
        """
        Calculates the maximum pair strength over all possible pairs of distinct indices.

        Parameters:
            nums (list[int]): An array of positive integers.

        Returns:
            int: The maximum strength computed across all distinct index pairs.
        """
        uniqueNums = sorted(set(nums), reverse = True)
        numCount = len(uniqueNums)

        if numCount < 2:
            return 1

        maxStrength = 0

        for firstIndex in range(numCount - 1):
            firstNum = uniqueNums[firstIndex]

            if firstNum * uniqueNums[firstIndex + 1] <= maxStrength:
                break

            for secondIndex in range(firstIndex + 1, numCount):
                secondNum = uniqueNums[secondIndex]

                if firstNum * secondNum <= maxStrength:
                    break

                commonDivisor = gcd(firstNum, secondNum)
                currentStrength = (firstNum // commonDivisor) * (secondNum // commonDivisor)

                if currentStrength > maxStrength:
                    maxStrength = currentStrength

        return maxStrength