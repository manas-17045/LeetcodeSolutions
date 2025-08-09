# Leetcode 231: Power of Two
# https://leetcode.com/problems/power-of-two/
# Solved on 9th of August, 2025
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        """
        Determines if a given integer is a power of two.

        Args:
            n (int): The integer to check.
        Returns:
            bool: True if n is a power of two, False otherwise.
        """
        return n > 0 and (n & (n - 1)) == 0