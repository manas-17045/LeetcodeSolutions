# Leetcode 3557: Find Maximum Number of Non Intersecting Substrings
# https://leetcode.com/problems/find-maximum-number-of-non-intersecting-substrings/
# Solved on 27th of September, 2025
class Solution:
    def maxSubstrings(self, word: str) -> int:
        """
        Calculates the maximum number of non-overlapping substrings of length at least 4
        where each substring starts and ends with the same character.

        Args:
            word: The input string.
        Returns:
            The maximum number of such substrings.
        """
        first = {}
        ans = 0

        for i, ch in enumerate(word):
            if ch not in first:
                # Record first occurrence of ch since the last reset.
                first[ch] = i
            else:
                # If substring from first[ch] to i has length >= 4, take it greedily.
                if i - first[ch] >= 3:
                    ans += 1
                    # Reset to enforce non-intersecting substrings
                    first.clear()

        return ans