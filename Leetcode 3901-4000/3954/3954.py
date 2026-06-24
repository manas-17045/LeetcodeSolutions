# Leetcode 3954: Sum of Compatible Numbers in Range I
# https://leetcode.com/problems/sum-of-compatible-numbers-in-range-i/
# Solved on 24th of June, 2026
class Solution:
    def sumOfGoodIntegers(self, n: int, k: int) -> int:
        """
        Calculates the sum of compatible numbers in the range.
        
        :param n: The base number.
        :param k: The range parameter.
        :return: The sum of compatible numbers in the range [max(1, n - k), n + k] such that (n & num) == 0.
        """
        totalSum = 0

        lowerBound = max(1, n - k)
        upperBound = n + k

        for currentNum in range(lowerBound, upperBound + 1):
            if (n & currentNum) == 0:
                totalSum += currentNum

        return totalSum