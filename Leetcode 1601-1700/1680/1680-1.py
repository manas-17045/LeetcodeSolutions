# Leetcode 1680: Concatenation of Consecutive Binary Numbers
# https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/
# Solved on 27th of August, 2025
class Solution:
    def concatenatedBinary(self, n: int) -> int:
        """
        Concatenates the binary representations of numbers from 1 to n and returns the decimal value
        of the resulting binary string, modulo 10^9 + 7.

        Args:
            n (int): The upper limit for concatenation.

        Returns:
            int: The decimal value of the concatenated binary string, modulo 10^9 + 7.
        """
        MOD = 10**9 + 7
        concatenatedValue = 0
        bitLength = 0
        for i in range(1, (n + 1)):
            if (i & (i - 1)) == 0:
                bitLength += 1
            concatenatedValue = ((concatenatedValue << bitLength) | i) % MOD
        return concatenatedValue