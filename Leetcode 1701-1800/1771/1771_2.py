# Leetcode 1771: Maximize Palindrome Length From Subsequence
# https://leetcode.com/problems/maximize-palindrome-length-from-subsequence/
# Solved on 18th of July, 2025
class Solution:
    def longestPalindrome(self, word1: str, word2: str) -> int:
        """
        Finds the length of the longest palindromic subsequence that can be formed
        by concatenating characters from `word1` and `word2`, such that at least
        one character is taken from `word1` and at least one character is taken
        from `word2`.

        Args:
            word1 (str): The first input string.
            word2 (str): The second input string.

        Returns:
            int: The length of the longest palindromic subsequence meeting the criteria.
        """
        s = word1 + word2
        n = len(s)
        L1 = len(word1)

        dp = [[0] * n for _ in range(n)]

        # Base case: single chars
        for i in range(n):
            dp[i][i] = 1

        # Fill dp in increasing order
        for i in range((n - 1), -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    # Skip either end
                    dp[i][j] = dp[i + 1][j] if dp[i + 1][j] > dp[i][j - 1] else dp[i][j - 1]

        # Now, enforce that we pick at least one char from word1 (index < L1),
        # And, at least one from word2 (index >= L1), by choosing matching endpoints.
        ans = 0
        for i in range(L1):
            for j in range(L1, n):
                if s[i] == s[j]:
                    inner = dp[i + 1][j - 1] if (i + 1) <= (j - 1) else 0
                    cand = inner + 2
                    if cand > ans:
                        ans = cand

        return ans