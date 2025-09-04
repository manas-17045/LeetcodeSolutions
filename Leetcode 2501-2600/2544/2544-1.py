# Leetcode 2544: Alternating Digit Sum
# https://leetcode.com/problems/alternating-digit-sum/
# Solved on 4th of September, 2025
class Solution:
    def alternateDigitSum(self, n: int) -> int:
        """
        Calculates the alternating digit sum of a given integer.
        :param n: The input integer.
        :return: The alternating digit sum.
        """
        s = str(n)
        totalSum = 0
        sign = 1
        for digitChar in s:
            digit = int(digitChar)
            totalSum += digit * sign
            sign *= -1
        return totalSum