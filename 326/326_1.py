# Leetcode 326: Power of Three
# https://leetcode.com/problems/power-of-three/
# Solved on 13th of August, 2025
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        """
        Determines if a given integer is a power of three.

        Args:
            n (int): The integer to check.
        Returns:
            bool: True if n is a power of three, False otherwise.
        """
        if n <= 0:
            return False

        maxPowerOfThree = 1162261467

        return maxPowerOfThree % n == 0