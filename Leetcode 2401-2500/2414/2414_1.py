# Leetcode 2414: Length of the Longest Alphabetical Continuous Substring
# https://leetcode.com/problems/length-of-the-longest-alphabetical-continuous-substring/
# Solved on 19th of August, 2025
class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        """
        Calculates the length of the longest alphabetical continuous substring.

        Args:
            s (str): The input string.
        Returns:
            int: The length of the longest continuous alphabetical substring.
        """
        if not s:
            return 0

        maxLength = 1
        currentLength = 1

        for i in range(1, len(s)):
            if ord(s[i]) == ord(s[i-1]) + 1:
                currentLength += 1
            else:
                currentLength = 1

            if currentLength > maxLength:
                maxLength = currentLength

        return maxLength