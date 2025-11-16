# Leetcode 1513: Number of Substrings With Only 1s
# https://leetcode.com/problems/number-of-substrings-with-only-1s/
# Solved on 16th of November, 2025
class Solution:
    def numSub(self, s: str) -> int:
        """
        Calculates the number of substrings consisting only of '1's in a binary string.

        Args:
            s: The input binary string.
        Returns:
            The total count of such substrings, modulo 10^9 + 7.
        """
        totalCount = 0
        currentLength = 0
        mod = 1000000007

        for char in s:
            if char == '1':
                currentLength += 1
                totalCount += currentLength
                totalCount %= mod
            else:
                currentLength = 0

        return totalCount