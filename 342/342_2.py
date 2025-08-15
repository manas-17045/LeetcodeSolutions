# Leetcode 342: Power of Four
# https://leetcode.com/problems/power-of-four/
# Solved on 15th of August, 2025
class Solution:
    def powerOfFour(self, n: int) -> bool:
        """
        Checks if a given integer `n` is a power of four.

        Args:
            n (int): The integer to check.
        Returns:
            bool: True if `n` is a power of four, False otherwise.
        """
        if n <= 0:
            return False
        # Check power of two
        if n & (n - 1):
            return False
        # Check that the single bit's position is even
        return ((n.bit_length() - 1) & 1) == 0