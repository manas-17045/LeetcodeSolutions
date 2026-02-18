# Leetcode 693: Binary Number with Alternating Bits
# https://leetcode.com/problems/binary-number-with-alternating-bits/
# Solved on 18th of February, 2026
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        """
        Checks if a positive integer has alternating bits.

        :param n: The input integer to check.
        :return: True if the bits alternate (e.g., 1010), False otherwise.
        """
        shiftedBits = n >> 1
        xorBits = n ^ shiftedBits
        return (xorBits & (xorBits + 1)) == 0