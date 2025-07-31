# Leetcode 940: Distinct Subsequences II
# https://leetcode.com/problems/distinct-subsequences-ii/
# Solved on 31st of July, 2025
class Solution:
    def distinctSubseqII(self, s: str) -> int:
        """
        Calculates the number of distinct non-empty subsequences of a given string `s`.

        Args:
            s (str): The input string consisting of lowercase English letters.
        Returns:
            int: The number of distinct non-empty subsequences modulo 10^9 + 7.
        """
        dp = [0] * 26
        totalSubsequences = 0
        mod = 10**9 + 7

        for char in s:
            charIndex = ord(char) - ord('a')
            oldCountForChar = dp[charIndex]

            newCountForChar = (totalSubsequences + 1) % mod

            dp[charIndex] = newCountForChar

            totalSubsequences = (totalSubsequences - oldCountForChar + newCountForChar + mod) % mod

        return totalSubsequences