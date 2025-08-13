# Leetcode 326: Power of Three
# https://leetcode.com/problems/power-of-three/
# Solved on 13th of August, 2025
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        """
        Checks if a given integer `n` is a power of three.

        Args:
            n (int): The integer to check.

        Returns:
            bool: True if `n` is a power of three, False otherwise.
        """
        return n > 0 and 1162261467 % n == 0