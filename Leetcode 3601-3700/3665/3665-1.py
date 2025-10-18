# Leetcode 3665: Twisted Mirror Path Count
# https://leetcode.com/problems/twisted-mirror-path-count/
# Solved on 17th of October, 2025
import sys
sys.setrecursionlimit(501000)


class Solution:
    def uniquePaths(self, grid: list[list[int]]) -> int:
        """
        Calculates the number of unique paths from (0,0) to (m-1, n-1) in a grid with twisted mirrors.

        Args:
            grid: A 2D list of integers representing the grid. 0 indicates an empty cell, 1 indicates a mirror.
        Returns:
            The number of unique paths modulo 10^9 + 7.
        """
        self.m = len(grid)
        self.n = len(grid[0])
        self.grid = grid
        self.mod = 10**9 + 7

        self.memoReflect = {}
        self.memoSolve = {}

        return self.solve(0, 0)

    def getReflectDest(self, r, c, entryDir):
        dirIdx = 0 if entryDir == "down" else 1
        state = (r, c, dirIdx)

        if not (0 <= r < self.m and 0 <= c < self.n):
            return (-1, -1)

        if self.grid[r][c] == 0:
            return (r, c)

        if state in self.memoReflect:
            if self.memoReflect[state] == (-2, -2):
                return (-1, -1)
            return self.memoReflect[state]

        self.memoReflect[state] = (-2, -2)

        res = (-1, -1)
        if entryDir == "down":
            res = self.getReflectDest(r, c + 1, "right")
        else:
            res = self.getReflectDest(r + 1, c, "down")

        self.memoReflect[state] = res
        return res

    def solve(self, r, c):
        if r == self.m - 1 and c == self.n - 1:
            return 1

        state = (r, c)
        if state in self.memoSolve:
            return self.memoSolve[state]

        paths = 0

        nr, nc = r, c + 1
        if nc < self. n:
            if self.grid[nr][nc] == 0:
                paths = (paths + self.solve(nr, nc)) % self.mod
            else:
                finalR, finalC = self.getReflectDest(nr + 1, nc, "down")
                if finalR != -1:
                    paths = (paths + self.solve(finalR, finalC)) % self.mod

        nr, nc = r + 1, c
        if nr < self.m:
            if self.grid[nr][nc] == 0:
                paths = (paths + self.solve(nr, nc)) % self.mod
            else:
                finalR, finalC = self.getReflectDest(nr, nc + 1, "right")
                if finalR != -1:
                    paths = (paths + self.solve(finalR, finalC)) % self.mod

        self.memoSolve[state] = paths
        return paths