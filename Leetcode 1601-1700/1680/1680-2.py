# Leetcode 1680: Concatenation of Consecutive Binary Numbers
# https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/
# Solved on 27th of August, 2025
class Solution:
    def concatenatedBinary(self, n: int) -> int:
        """
        Concatenates the binary representations of numbers from 1 to n and returns the decimal value modulo 10^9 + 7.
        :param n: An integer.
        :return: The decimal value of the concatenated binary string modulo 10^9 + 7.
        """
        MOD = 10**9 + 7
        res = 0
        bits = 0
        for i in range(1, n + 1):
            # Increment bits when i is a power of two
            if (i & (i - 1)) == 0:
                bits += 1
            res = ((res << bits) | i) % MOD
        return res