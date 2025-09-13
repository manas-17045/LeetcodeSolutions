# Leetcode 1162: As Far from Land as Possible
# https://leetcode.com/problems/as-far-from-land-as-possible/
# Solved on 13th of September, 2025
import collections


class Solution:
    def maxDistance(self, grid: list[list[int]]) -> int:
        """
        Finds the maximum Manhattan distance from a land cell (1) to a water cell (0) in a grid.
        If there are no land cells or no water cells, returns -1.

        Args:
            grid (list[list[int]]): A square grid where 1 represents land and 0 represents water.

        Returns:
            int: The maximum Manhattan distance, or -1 if no land or no water exists.
        """
        gridSize = len(grid)
        queue = collections.deque()

        for row in range(gridSize):
            for col in range(gridSize):
                if grid[row][col] == 1:
                    queue.append((row, col))

        if not queue or len(queue) == gridSize * gridSize:
            return -1

        distance = -1
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while queue:
            distance += 1
            levelSize = len(queue)
            for _ in range(levelSize):
                row, col = queue.popleft()

                for dr, dc in directions:
                    newRow = row + dr
                    newCol = col + dc

                    if 0 <= newRow < gridSize and 0 <= newCol < gridSize and grid[newRow][newCol] == 0:
                        grid[newRow][newCol] = 1
                        queue.append((newRow, newCol))

        return distance