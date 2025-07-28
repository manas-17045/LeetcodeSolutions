# Leetcode 2223: Sum of Scores of Built Strings
# https://leetcode.com/problems/sum-of-scores-of-built-strings/
# Solved on 28th of July, 2025
class Solution:
    def sumScores(self, s: str) -> int:
        """
        Calculates the sum of scores for all prefixes of a given string s.
        The score of a string is defined as the length of its longest common prefix with s.
        This is efficiently computed using the Z-algorithm.

        Args:
            s (str): The input string.
        Returns:
            int: The sum of scores for all prefixes of s.
        """
        n = len(s)
        z = [0] * n
        l = r = 0

        # Build Z-array
        for i in range(1, n):
            if i <= r:
                # Mirror value or remaining window
                z[i] = min(r - i + 1, z[i - l])
            # Try to extend match past current [l...r]
            while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                z[i] += 1
            # If we extended past r, update [l...r]
            if i + z[i] - 1 > r:
                l = i
                r = i + z[i] - 1

        # Sum of all Z-values plus the full string match (which is n).
        return sum(z) + n