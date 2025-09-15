# Leetcode 3472: Longest Palindromic Subsequence After at Most K Operations
# https://leetcode.com/problems/longest-palindromic-subsequence-after-at-most-k-operations/
# Solved on 15th of September, 2025
from functools import lru_cache


class Solution:
    def longestPalindromicSubsequence(self, s: str, k: int) -> int:
        """
        Finds the length of the longest palindromic subsequence of `s` such that the total cost of changing characters
        to make it a palindrome does not exceed `k`.
        :param s: The input string.
        :param k: The maximum allowed cost for character changes.
        :return: The length of the longest palindromic subsequence.
        """
        n = len(s)
        # Convert to ordinal values for faster distance calculation
        vals = [ord(ch) for ch in s]

        def cost(a_ord, b_ord):
            diff = abs(a_ord - b_ord)
            return min(diff, 26 - diff)

        @lru_cache(maxsize=None)
        def dp(i: int, j: int, rem: int) -> int:
            if i > j:
                return 0
            if i == j:
                # Single character always gives palindrome length 1
                return 1

            # Skip either side (Take best subsequence skipping left or right)
            best = max(dp(i + 1, j, rem), dp(i, j - 1, rem))

            # If characters already equal, take both
            if vals[i] == vals[j]:
                best = max(best, 2 + dp(i + 1, j - 1, rem))
            else:
                c = cost(vals[i], vals[j])
                if c <= rem:
                    best = max(best, 2 + dp(i + 1, j - 1, rem - c))

            return best

        return dp(0, n - 1, k)