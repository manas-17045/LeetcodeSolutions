# Leetcode 1638: Count Substrings That Differ by One Character
# https://leetcode.com/problems/count-substrings-that-differ-by-one-character/
# Solved on 23rd of July, 2025
class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        """
        Counts the number of pairs of substrings (sub_s, sub_t) such that sub_s is a substring of s,
        sub_t is a substring of t, sub_s and sub_t have the same length, and they differ by exactly one character.

        Args:
            s (str): The first input string.
            t (str): The second input string.

        Returns:
            int: The total count of such pairs of substrings.
        """
        n, m = len(s), len(t)

        dp1 = [[0] * (m +1) for _ in range(n + 1)]
        for i in range(1, (n + 1)):
            for j in range(1, (m + 1)):
                if s[i - 1] == t[j - 1]:
                    dp1[i][j] = dp1[i - 1][j - 1] + 1

        dp2 = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range((n - 1), -1, -1):
            for j in range((m - 1), -1, -1):
                if s[i] == t[j]:
                    dp2[i][j] = dp2[i + 1][j + 1] + 1

        ans = 0
        # For every mismatch, count all ways to pick equal-length
        # substrings extending around that mismatch
        for i in range(n):
            for j in range(m):
                if s[i] != t[j]:
                    left = dp1[i][j]
                    right = dp2[i + 1][j + 1]
                    ans += (left + 1) * (right + 1)

        return ans