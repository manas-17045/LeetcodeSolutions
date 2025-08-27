# Leetcode 3459: Length of Longest V-Shaped Diagonal Segment
# https://leetcode.com/problems/length-of-longest-v-shaped-diagonal-segment/
# Solved on 27th of August, 2025
import sys
from functools import lru_cache


class Solution:
    def lenOfVDiagonal(self, grid: list[list[int]]) -> int:
        """
        Calculates the maximum length of a "V-diagonal" in a given grid.

        Args:
            grid: A list of lists of integers representing the grid. Each cell contains either 1 or 2.
        Returns:
            The maximum length of a V-diagonal found in the grid.
        """
        # Handle empty grid
        if not grid or not grid[0]:
            return 0

        sys.setrecursionlimit(10 ** 6)
        m, n = len(grid), len(grid[0])
        DIRS = [(-1, 1), (1, 1), (1, -1), (-1, -1)]

        # Memoized DFS
        @lru_cache(None)
        def dfs(i: int, j: int, turned: int, num: int, dir: int) -> int:
            if i < 0 or i >= m or j < 0 or j >= n:
                return 0
            if grid[i][j] != num:
                return 0

            next_num = 0 if num == 2 else 2
            dx, dy = DIRS[dir]

            # Continue straight
            res = 1 + dfs(i + dx, j + dy, turned, next_num, dir)

            # Optionally turn once (clockwise)
            if turned == 0:
                next_dir = (dir + 1) % 4
                ndx, ndy = DIRS[next_dir]
                res = max(res, 1 + dfs(i + ndx, j + ndy, 1, next_num, next_dir))

            return res

        ans = 0
        # Start from every cell with value 1 and try all 4 diagonal directions
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    for d, (dx, dy) in enumerate(DIRS):
                        ans = max(ans, 1 + dfs(i + dx, j + dy, 0, 2, d))

        return ans