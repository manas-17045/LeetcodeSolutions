# Leetcode 1771: Maximize Palindrome Length From Subsequence
# https://leetcode.com/problems/maximize-palindrome-length-from-subsequence/
# Solved on 18th of July, 2025
class Solution:
    def longestPalindrome(self, word1: str, word2: str) -> int:
        """
        Calculates the length of the longest palindrome that can be formed by concatenating
        a subsequence from word1 and a subsequence from word2.

        Args:
            word1 (str): The first input string.
            word2 (str): The second input string.
        Returns:
            int: The maximum length of the palindrome.
        """
        s = word1 + word2
        n = len(s)
        len1 = len(word1)
        dp = [[0] * n for _ in range(n)]
        maxLength = 0

        for i in range(n):
            dp[i][i] = 1

        for length in range(2, (n + 1)):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i + 1][j - 1]
                    if (i < len1) and (j >= len1):
                        maxLength = max(maxLength, dp[i][j])
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return maxLength