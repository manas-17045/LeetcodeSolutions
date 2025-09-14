# Leetcode 1970: Last Day Where You Can Still Cross
# https://leetcode.com/problems/last-day-where-you-can-still-cross/
# Solved on 14th of September, 2025
from collections import deque


class Solution:
    def latestDayToCross(self, row: int, col: int, cells: list[list[int]]) -> int:
        """
        Finds the latest day a person can cross from the top row to the bottom row of a grid.
        Args:
            row (int): The number of rows in the grid.
            col (int): The number of columns in the grid.
            cells (list[list[int]]): A list of cells that will be flooded, ordered by day.
        Returns:
            int: The latest day a person can cross the grid.
        """
        def canCross(day: int) -> bool:
            grid = [[0] * col for _ in range(row)]
            for i in range(day):
                r, c = cells[i][0] - 1, cells[i][1] - 1
                grid[r][c] = 1

            queue = deque()
            visited = set()

            for c in range(col):
                if grid[0][c] == 0:
                    queue.append((0, c))
                    visited.add((0, c))

            while queue:
                r, c = queue.popleft()
                if r == row - 1:
                    return True

                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    newR, newC = r + dr, c + dc
                    if 0 <= newR < row and 0 <= newC < col and grid[newR][newC] == 0 and (newR, newC) not in visited:
                        visited.add((newR, newC))
                        queue.append((newR, newC))

            return False

        low, high = 1, len(cells)
        ans = 0
        while low <= high:
            mid = low + (high - low) // 2
            if canCross(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans