# Leetcode 1404: Number of Steps to Reduce a Number in Binary Representation to One
# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/
# Solved on 26th of February, 2026
class Solution:
    def numSteps(self, s: str) -> int:
        """
        Calculates the number of steps to reduce a binary string to one.

        :param s: A string representing a binary number.
        :return: The total number of operations (divide by 2 if even, add 1 if odd) required.
        """
        totalSteps = 0
        carryBit = 0

        for stringIndex in range(len(s) - 1, 0, -1):
            currentSum = int(s[stringIndex]) + carryBit
            if currentSum == 1:
                totalSteps += 2
                carryBit = 1
            else:
                totalSteps += 1
                carryBit = currentSum // 2

        return totalSteps + carryBit