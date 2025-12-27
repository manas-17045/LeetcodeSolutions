# Leetcode 3713: Longest Balanced Substring I
# https://leetcode.com/problems/longest-balanced-substring-i/
# Solved on 27th of December, 2025
class Solution:
    def longestBalanced(self, s: str) -> int:
        """
        Finds the length of the longest balanced substring.

        Args:
            s: The input string.
        Returns:
            The length of the longest balanced substring.
        """
        n = len(s)

        maxLen = 0
        for i in range(n):
            freq = {}

            for j in range(i, n):
                char = s[j]
                freq[char] = freq.get(char, 0) + 1
                counts = list(freq.values())

                if len(set(counts)) == 1:
                    maxLen = max(maxLen, j - i + 1)

        return maxLen