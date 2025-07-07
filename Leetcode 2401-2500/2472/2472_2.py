# Leetcode 2472: Maximum Number of Non-overlapping Palindrome Substrings
# https://leetcode.com/problems/maximum-number-of-non-overlapping-palindrome-substrings/
# Solved on 7th of July, 2025
import sys
from functools import lru_cache


class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        """
        Calculates the maximum number of non-overlapping palindromic substrings
        of length at least k.

        This method uses a two-step dynamic programming approach. First, it
        pre-computes all possible palindromic substrings within s and stores
        the results in a 2D boolean array `is_pal`.

        Second, it uses a memoized recursive function (DFS) to determine the
        maximum number of palindromes. The function `dfs(i)` computes the max
        palindromes in the suffix `s[i:]`. At each index `i`, it decides
        between two options:
        1. Skip the character at `i` and find the max palindromes from `i+1`.
        2. Find a palindrome of length at least `k` starting at `i`. If one
           is found ending at `j`, take `1 + dfs(j + 1)`.

        The function returns the maximum value found from these choices,
        starting the process from index 0.

        Args:
            s: The input string.
            k: The minimum length of a palindromic substring.

        Returns:
            The maximum number of non-overlapping palindromic substrings of
            length at least k.
        """
        n = len(s)
        if k > n:
            return 0

        is_pal = [[False] * n for _ in range(n)]
        for i in range(n):
            is_pal[i][i] = True
        for i in range(n - 1):
            is_pal[i][i + 1] = (s[i] == s[i + 1])

        for length in range(3, (n + 1)):
            for i in range(n - length + 1):
                j = i + length - 1

                if s[i] == s[j] and is_pal[i + 1][j - 1]:
                    is_pal[i][j] = True

        # Memoized DFS TO choose non-overlapping palindromes
        sys.setrecursionlimit(10000)
        @lru_cache(None)
        def dfs(i: int) -> int:
            if i >= n:
                return 0

            best = dfs(i + 1)
            end = i + k - 1
            for j in range(end, n):
                if is_pal[i][j]:
                    best = max(best, (1 + dfs(j + 1)))
            return best

        return dfs(0)