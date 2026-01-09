# Leetcode 3797: Count Routes to Climb a Rectangular Grid
# https://leetcode.com/problems/count-routes-to-climb-a-rectangular-grid/
# Solved on 9th of January, 2026
import math


class Solution:
    def numberOfRoutes(self, grid: list[str], d: int) -> int:
        """
        Calculates the number of routes to climb a rectangular grid.

        Args:
            grid: A list of strings representing the grid, where '.' denotes an empty cell
                  and '#' denotes an obstacle.
            d: The maximum horizontal distance a jump can cover.

        Returns:
            The total number of valid routes to climb the grid, modulo 10^9 + 7.
        """
        mod = 10 ** 9 + 7
        rows = len(grid)
        cols = len(grid[0])

        if d >= 1:
            vertMax = int(math.isqrt(d * d - 1))
        else:
            vertMax = -1

        v = [0] * cols
        for c in range(cols):
            if grid[rows - 1][c] == '.':
                v[c] = 1

        def getPrefixSum(arr):
            p = [0] * (cols + 1)
            for i in range(cols):
                p[i + 1] = (p[i] + arr[i]) % mod
            return p

        def rangeSum(p, l, r):
            l = max(0, l)
            r = min(cols - 1, r)
            if l > r:
                return 0
            return (p[r + 1] - p[l]) % mod

        prefixV = getPrefixSum(v)
        h = [0] * cols
        t = [0] * cols

        for c in range(cols):
            if grid[rows - 1][c] == '.':
                total = rangeSum(prefixV, c - d, c + d)
                h[c] = (total - v[c] + mod) % mod
                t[c] = (v[c] + h[c]) % mod

        for r in range(rows - 2, -1, -1):
            prevT = t
            prefixPrevT = getPrefixSum(prevT)

            newV = [0] * cols

            if vertMax >= 0:
                for c in range(cols):
                    if grid[r][c] == '.':
                        newV[c] = rangeSum(prefixPrevT, c - vertMax, c + vertMax)

            prefixNewV = getPrefixSum(newV)
            newH = [0] * cols
            newT = [0] * cols

            for c in range(cols):
                if grid[r][c] == '.':
                    total = rangeSum(prefixNewV, c - d, c + d)
                    newH[c] = (total - newV[c] + mod) % mod
                    newT[c] = (newV[c] + newH[c]) % mod

            t = newT

        return sum(t) % mod