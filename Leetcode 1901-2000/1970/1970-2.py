# Leetcode 1970: Last Day Where You Can Still Cross
# https://leetcode.com/problems/last-day-where-you-can-still-cross/
# Solved on 14th of September, 2025
from collections import deque


class Solution:
    def latestDayToCross(self, row: int, col: int, cells: list[list[int]]) -> int:
        """
        Finds the latest day a person can cross from the top row to the bottom row of a grid.
        :param row: The number of rows in the grid.
        :param col: The number of columns in the grid.
        :param cells: A list of lists, where each inner list [r, c] represents a cell that turns into water on a specific day.
        :return: The latest day a person can cross the grid.
        """
        def canCross(day: int) -> bool:
            grid = [[0] * col for _ in range(row)]
            # Mark flooded cells
            for i in range(day):
                r, c = cells[i]
                grid[r - 1][c - 1] = 1

            q = deque()
            # Push all land cells in top row
            for j in range(col):
                if grid[0][j] == 0:
                    q.append((0, j))
                    grid[0][j] = 1

            while q:
                r0, c0 = q.popleft()
                if r0 == row - 1:
                    return True

                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = r0 + dr, c0 + dc
                    if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 0:
                        grid[nr][nc] = 1
                        q.append((nr, nc))

            return False

        lo, hi = 0, row * col
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if canCross(mid):
                lo = mid
            else:
                hi = mid - 1

        return lo