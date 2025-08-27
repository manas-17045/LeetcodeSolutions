# Leetcode 3459: Length of Longest V-Shaped Diagonal Segment
# https://leetcode.com/problems/length-of-longest-v-shaped-diagonal-segment/
# Solved on 27th of August, 2025
from functools import lru_cache


class Solution:
    def lenOfVDiagonal(self, grid: list[list[int]]) -> int:
        """
        Calculates the length of the longest V-shaped diagonal segment in a grid.

        Args:
            grid: A 2D list of integers representing the grid.
        Returns:
            The length of the longest V-shaped diagonal segment.
        """
        m, n = len(grid), len(grid[0])
        dirs = [(-1, 1), (1, 1), (1, -1), (-1, -1)]

        @lru_cache(None)
        def dfs(i: int, j: int, turned: bool, num: int, direction: int) -> int:
            if not (0 <= i < m and 0 <= j < n and grid[i][j] == num):
                return 0

            next_num = 0 if num == 2 else 2

            dx, dy = dirs[direction]
            res = 1 + dfs(i + dx, j + dy, turned, next_num, direction)

            if not turned:
                next_dir = (direction + 1) % 4
                next_dx, next_dy = dirs[next_dir]
                res = max(res, 1 + dfs(i + next_dx, j + next_dy, True, next_num, next_dir))

            return res

        max_len = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    max_len = max(max_len, 1)
                    for d in range(4):
                        dx, dy = dirs[d]
                        max_len = max(max_len, 1 + dfs(r + dx, c + dy, False, 2, d))

        return max_len