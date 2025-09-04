# Leetcode 2544: Alternating Digit Sum
# https://leetcode.com/problems/alternating-digit-sum/
# Solved on 4th of September, 2025
class Solution:
    def alternateDigitSum(self, n: int) -> int:
        """
        Calculates the alternating digit sum of an integer.
        :param n: The input integer.
        :return: The alternating digit sum.
        """
        # Find highest power of 10 <= n
        p = 1
        while p * 10 <= n:
            p *= 10

        total = 0
        # Most significant digit is positive
        sign = 1
        while p > 0:
            digit = n // p
            total += sign * digit
            n %= p
            p //= 10
            sign = -sign

        return total