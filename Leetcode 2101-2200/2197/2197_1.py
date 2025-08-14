# Leetcode 2197: Replace Non-Coprime Numbers in Array
# https://leetcode.com/problems/replace-non-coprime-numbers-in-array/
# Solved on 14th of August, 2025
import math


class Solution:
    def replaceNonCoprimes(self, nums: list[int]) -> list[int]:
        """
        Replaces non-coprime numbers in an array according to specific rules.
        If two adjacent numbers are not coprime (their greatest common divisor > 1),
        they are replaced by their least common multiple (LCM). This process
        repeats until all adjacent numbers are coprime.

        Args:
            nums: A list of integers.

        Returns:
            A list of integers where all adjacent numbers are coprime.
        """

        resultStack = []

        for num in nums:
            currentNum = num
            while resultStack:
                stackTop = resultStack[-1]
                commonDivisor = math.gcd(currentNum, stackTop)
                if commonDivisor > 1:
                    resultStack.pop()
                    currentNum = (currentNum * stackTop) // commonDivisor
                else:
                    break
            resultStack.append(currentNum)

        return resultStack