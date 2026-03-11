# Leetcode 1009: Complement of Base 10 Integer
# https://leetcode.com/problems/complement-of-base-10-integer/
# Solved on 11th of March, 2026
class Solution:
    def bitwiseComplement(self, n: int) -> int:
        """
        Computes the bitwise complement of a base-10 integer.
        :param n: The input integer.
        :return: The integer representing the bitwise complement of n.
        """
        if n == 0:
            return 1

        bitLength = n.bit_length()
        bitMask = (1 << bitLength) - 1

        return n ^ bitMask