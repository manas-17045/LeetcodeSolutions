# Leetcode 1293: Shortest Path in a Grid with Obstacles Elimination
# https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/
# Solved on 1st of December, 2025
from collections import deque


class Solution:
    def shortestPath(self, grid: list[list[int]], k: int) -> int:
        """
        Finds the shortest path from the top-left corner to the bottom-right corner of a grid,
        allowing for the elimination of at most `k` obstacles.

        Args:
            grid (list[list[int]]): A 2D grid where 0 represents an empty cell and 1 represents an obstacle.
            k (int): The maximum number of obstacles that can be eliminated.

        Returns:
            int: The length of the shortest path, or -1 if no such path exists.
        """
        rows = len(grid)
        cols = len(grid[0])

        if k >= rows + cols - 2:
            return rows + cols - 2

        queue = deque([(0, 0, k, 0)])
        visited = [[-1] * cols for _ in range(rows)]
        visited[0][0] = k
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while queue:
            row, col, curK, dist = queue.popleft()

            if row == rows - 1 and col == cols - 1:
                return dist

            for dRow, dCol in directions:
                newRow, newCol = row + dRow, col + dCol

                if 0 <= newRow < rows and 0 <= newCol < cols:
                    newK = curK - grid[newRow][newCol]

                    if newK >= 0 and newK > visited[newRow][newCol]:
                        visited[newRow][newCol] = newK
                        queue.append((newRow, newCol, newK, dist + 1))

        return -1