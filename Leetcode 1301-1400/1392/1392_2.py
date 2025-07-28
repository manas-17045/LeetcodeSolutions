# Leetcode 1392: Longest Happy Prefix
# https://leetcode.com/problems/longest-happy-prefix/
# Solved on 28th of July, 2025
class Solution:
    def longestPrefix(self, s: str) -> str:
        """
        Finds the longest prefix of a string that is also a suffix of the same string (excluding the string itself).
        :param s: The input string.
        :return: The longest prefix that is also a suffix.
        """
        n = len(s)
        lps = [0] * n
        # Length of the previous longest prefix-suffix
        j = 0

        # Build the lps array
        for i in range(1, n):
            # Fall back in the pattern until we match or reach 0
            while j > 0 and s[i] != s[j]:
                j = lps[j - 1]
            if s[i] == s[j]:
                j += 1
                lps[i] = j

        # The value at lps[-1] is the length of the longest happy prefix
        return s[:lps[-1]]