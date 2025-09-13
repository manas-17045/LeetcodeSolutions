# Leetcode 1162: As Far from Land as Possible
# https://leetcode.com/problems/as-far-from-land-as-possible/
# Solved on 13th of September, 2025
from collections import deque


class Solution:
    def maxDistance(self, grid: list[list[int]]) -> int:
        """
        Calculates the maximum distance from a land cell (1) to the nearest water cell (0) in a grid.
        :param grid: A 2D list of integers representing the grid, where 1 is land and 0 is water.
        :return: The maximum distance from a land cell to the nearest water cell.
                 Returns -1 if there is no land or no water in the grid.
        """
        n = len(grid)
        q = deque()

        # Push all land cells into queue
        land_count = 0
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    q.append((r, c))
                    land_count += 1

        # If no land or no water, return -1.
        if land_count == 0 or land_count == n * n:
            return -1

        # BFS directions
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        dist = -1

        # Expand BFS level by level; each level increases distance by 1
        while q:
            level_size = len(q)
            for _ in range(level_size):
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                        grid[nr][nc] = 1
                        q.append((nr, nc))
            dist += 1

        return dist