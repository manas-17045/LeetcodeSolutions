# Leetcode 2730: Find the Longest Semi-Repetitive Substring
# https://leetcode.com/problems/find-the-longest-semi-repetitive-substring/
# Solved on 8th of January, 2026
class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        """
        Finds the length of the longest semi-repetitive substring.

        A string is semi-repetitive if it has at most one pair of adjacent identical characters.

        Args:
            s (str): The input string.
        Returns:
            int: The length of the longest semi-repetitive substring.
        """
        start = 0
        repeatCount = 0
        maxLength = 1

        for end in range(1, len(s)):
            if s[end] == s[end - 1]:
                repeatCount += 1

            while repeatCount > 1:
                if s[start] == s[start + 1]:
                    repeatCount -= 1
                start += 1

            maxLength = max(maxLength, end - start + 1)

        return maxLength