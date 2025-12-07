# Leetcode 2370: Longest Ideal Subsequence
# https://leetcode.com/problems/longest-ideal-subsequence/
# Solved on 7th of December, 2025
class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        """
        Finds the length of the longest ideal subsequence.

        An ideal subsequence is a subsequence where the absolute difference between the
        ordinal values of any two adjacent characters is less than or equal to k.

        Args:
            s (str): The input string.
            k (int): The maximum allowed difference between adjacent characters.

        Returns:
            int: The length of the longest ideal subsequence.
        """
        dp = [0] * 26
        base = ord('a')
        for char in s:
            curr = ord(char) - base
            lower = max(0, curr - k)
            upper = min(26, curr + k + 1)

            longestPrev = 0
            for i in range(lower, upper):
                if dp[i] > longestPrev:
                    longestPrev = dp[i]

            dp[curr] = longestPrev + 1

        return max(dp)