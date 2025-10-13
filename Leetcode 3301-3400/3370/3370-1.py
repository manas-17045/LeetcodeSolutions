# Leetcode 3370: Smallest Number With All Set Bits
# https://leetcode.com/problems/smallest-number-with-all-set-bits/
# Solved on 13th of October, 2025
class Solution:
    def smallestNumber(self, n: int) -> int:
        """
        Given an integer n, return the smallest positive integer that has all its bits set,
        and is greater than or equal to n.
        :param n: The input integer.
        :return: The smallest positive integer with all bits set, greater than or equal to n.
        """
        numberOfBits = n.bit_length()
        result = (1 << numberOfBits) - 1
        return result