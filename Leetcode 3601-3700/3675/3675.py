# Leetcode 3675: Minimum Operations to Transform String
# https://leetcode.com/problems/minimum-operations-to-transform-string/
# Solved on 28th of December, 2025
class Solution:
    def minOperations(self, s: str) -> int:
        """
        Calculates the minimum operations to transform a string.

        Args:
            s (str): The input string.
        Returns:
            int: The minimum number of operations.
        """
        charSet = set(s)
        if 'a' in charSet:
            charSet.remove('a')

        if not charSet:
            return 0

        minChar = min(charSet)
        return 26 - (ord(minChar) - ord('a'))