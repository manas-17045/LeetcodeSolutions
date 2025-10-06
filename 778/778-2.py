# Leetcode 778: Swim in Rising Water
# https://leetcode.com/problems/swim-in-rising-water/
# Solved on 6th of October, 2025
import heapq


class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        """
        Finds the least time until a path exists from the top-left to the bottom-right cell.

        Args:
            grid (list[list[int]]): An n x n integer matrix where grid[i][j] represents the elevation at (i, j).
        Returns:
            int: The least time until a path exists.
        """
        n = len(grid)

        # Priority queue
        pq = [(grid[0][0], 0, 0)]
        visited = set()
        visited.add((0, 0))

        # Directions
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while pq:
            time, row, col = heapq.heappop(pq)

            # If we reached the bottom-right corner
            if row == n - 1 and col == n - 1:
                return time

            # Explore all 4 adjacent neighbors
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc

                # Check if the nw position is valid and not visited
                if 0 <= new_row < n and 0 <= new_col < n and (new_row, new_col) not in visited:
                    visited.add((new_row, new_col))

                    # The time needed is the max of current time and the elevation at new cell.
                    new_time = max(time, grid[new_row][new_col])
                    heapq.heappush(pq, (new_time, new_row, new_col))

        # Should never reach here if input is valid
        return -1