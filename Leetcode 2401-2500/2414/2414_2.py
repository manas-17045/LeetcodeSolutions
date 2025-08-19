# Leetcode 2414: Length of the Longest Alphabetical Continuous Substring
# https://leetcode.com/problems/length-of-the-longest-alphabetical-continuous-substring/
# Solved on 19th of August, 2025
class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        """
        Calculates the length of the longest continuous alphabetical substring.

        Args:
            s (str): The input string.
        Returns:
            int: The length of the longest continuous alphabetical substring.
        """
        # If string is empty, answer is 0.
        if not s:
            return 0

        max_len = 1
        curr_len = 1

        # Walk through string once, comparing consecutive characters
        for i in range(1, len(s)):
            # Check if current char continues the alphabetical sequence
            if ord(s[i]) == ord(s[i - 1]) + 1:
                curr_len += 1
            else:
                curr_len = 1

            if curr_len > max_len:
                max_len = curr_len

        return max_len