# Leetcode 1444: Number of Ways of Cutting a Pizza
# https://leetcode.com/problems/number-of-ways-of-cutting-a-pizza/
# Solved on 11th of September, 2025
from functools import lru_cache


class Solution:
    def ways(self, pizza: list[str], k: int) -> int:
        """
        Calculates the number of ways to cut a pizza into k pieces such that each piece contains at least one apple.

        Args:
            pizza: A list of strings representing the pizza, where 'A' denotes an apple and '.' denotes an empty space.
            k: The number of pieces to cut the pizza into.
        Returns:
            The number of ways to cut the pizza, modulo 10^9 + 7.
        """
        MOD = 10 ** 9 + 7
        R, C = len(pizza), len(pizza[0])

        # apples[i][j] = number of 'A's in submatrix with top-left at (i,j) to bottom-right
        apples = [[0] * (C + 1) for _ in range(R + 1)]
        for i in range(R - 1, -1, -1):
            for j in range(C - 1, -1, -1):
                apples[i][j] = (
                        (1 if pizza[i][j] == 'A' else 0)
                        + apples[i + 1][j]
                        + apples[i][j + 1]
                        - apples[i + 1][j + 1]
                )

        @lru_cache(None)
        def dp(i: int, j: int, pieces: int) -> int:
            # If no apples in this submatrix, no valid way
            if apples[i][j] == 0:
                return 0
            # If only one piece needed and this submatrix has at least one apple -> 1 way
            if pieces == 1:
                return 1

            res = 0
            # Try horizontal cuts: cut between row r-1 and r (r from i+1 .. R-1)
            for r in range(i + 1, R):
                # top piece = rows i..r-1. Check it has at least one apple:
                if apples[i][j] - apples[r][j] > 0:
                    res += dp(r, j, pieces - 1)
                    if res >= MOD:
                        res -= MOD

            # Try vertical cuts: cut between col c-1 and c (c from j+1 .. C-1)
            for c in range(j + 1, C):
                # left piece = cols j..c-1. Check it has at least one apple:
                if apples[i][j] - apples[i][c] > 0:
                    res += dp(i, c, pieces - 1)
                    if res >= MOD:
                        res -= MOD

            return res % MOD

        return dp(0, 0, k)