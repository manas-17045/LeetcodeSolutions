# Leetcode 342: Power of Four
# https://leetcode.com/problems/power-of-four/
# Solved on 15th of August, 2025
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        """
        Determines if a given integer is a power of four.

        Args:
            n (int): The integer to check.
        Returns:
            bool: True if n is a power of four, False otherwise.
        """
        if n <= 0:
            return False

        isPowerOfTwo = (n & (n -1)) == 0
        if not isPowerOfTwo:
            return False

        isCorrectBitPosition = (n & 0x55555555) != 0
        return isCorrectBitPosition