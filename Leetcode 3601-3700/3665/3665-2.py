# Leetcode 3665: Twisted Mirror Path Count
# https://leetcode.com/problems/twisted-mirror-path-count/
# Solved on 18th of October, 2025
import sys
from functools import lru_cache


class Solution:
    def uniquePaths(self, grid: list[list[int]]) -> int:
        """
        Calculates the number of unique paths from the top-left corner (0, 0) to the bottom-right corner (m-1, n-1)
        of a grid, where '0' represents an empty cell and '1' represents an obstacle.
        :param grid: A 2D list of integers representing the grid.
        :return: The number of unique paths modulo 10^9 + 7.
        """
        sys.setrecursionlimit(10000)
        MOD = 10**9 + 7
        m = len(grid)
        n = len(grid[0])

        dr = (0, 1)
        dc = (1, 0)

        @lru_cache(None)
        def next_dest(i: int, j: int, dir: int) -> tuple[int, int]:

            pi = i + dr[dir]
            pj = j + dc[dir]
            while 0 <= pi < m and 0 <= pj < n:
                if grid[pi][pj] == 0:
                    return (pi, pj)

                if dir == 0:
                    dir = 1
                    pi = pi + 1
                else:
                    dir = 0
                    pj = pj + 1

            return (-1, -1)

        @lru_cache(None)
        def dp(i: int, j: int) -> int:
            if i == m - 1 and j == n - 1:
                return 1
            total = 0

            for dir in (0, 1):
                ni, nj = next_dest(i, j, dir)
                if ni == -1:
                    continue
                total = (total + dp(ni, nj)) % MOD

            return total

        return dp(0, 0)