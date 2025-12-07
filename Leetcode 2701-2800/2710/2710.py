# Leetcode 2710: Remove Trailing Zeros From a String
# https://leetcode.com/problems/remove-trailing-zeros-from-a-string/
# Solved on 7th of December, 2025
class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        """
        Removes all trailing zeros from a string representing a non-negative integer.

        Args:
            num (str): A string representing a non-negative integer.

        Returns:
            str: The string with all trailing zeros removed.
        """
        return num.rstrip('0')