# Leetcode 190: Reverse Bits
# https://leetcode.com/problems/reverse-bits/
# Solved on 16th of February, 2026
class Solution:
    def reverseBits(self, n: int) -> int:
        """
        Reverses the bits of a given 32-bit unsigned integer.

        :param n: A 32-bit unsigned integer.
        :return: The integer formed by reversing the bits of n.
        """
        reversedValue = 0

        for _ in range(32):
            reversedValue = (reversedValue << 1) | (n & 1)
            n >>= 1

        return reversedValue