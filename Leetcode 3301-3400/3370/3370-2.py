# Leetcode 3370: Smallest Number With All Set Bits
# https://leetcode.com/problems/smallest-number-with-all-set-bits/
# Solved on 13th of October, 2025
class Solution:
    def smallestNumber(self, n: int) -> int:
        """
        Finds the smallest integer x such that x >= n and all bits in x are set to 1.
        :param n: The input integer.
        :return: The smallest integer x with all bits set to 1, such that x >= n.
        """
        bits = n.bit_length()

        # Create a number with all bits set (2^bits - 1)
        candidate = (1 << bits) - 1

        # If candidate >= n, return it; else, we need one more bit
        return candidate if candidate >= n else ((1 << (bits + 1)) - 1)