# Leetcode 1631: Path With Minimum Effort
# https://leetcode.com/problems/path-with-minimum-effort/
# Solved on 6th of October, 2025
import heapq


class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        """
        Finds the minimum effort required to travel from the top-left cell to the bottom-right cell of a 2D grid.
        The effort of a path is defined as the maximum absolute difference in heights between any two adjacent cells along the path.

        Args:
            heights (list[list[int]]): A 2D list of integers representing the height of each cell.
        Returns:
            int: The minimum effort required to reach the bottom-right cell.
        """
        rows = len(heights)
        cols = len(heights[0])

        # Priority queue
        pq = [(0, 0, 0)]

        # Track minimum effort to reach each cell
        min_effort = [[float('inf')] * cols for _ in range(rows)]
        min_effort[0][0] = 0

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while pq:
            effort, row, col = heapq.heappop(pq)

            # If we reached the destination
            if row == rows - 1 and col == cols - 1:
                return effort

            # Skip if we've already found a better path to this cell
            if effort > min_effort[row][col]:
                continue

            # Explore neighbors
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc

                # Check bounds
                if 0 <= new_row < rows and 0 <= new_col < cols:
                    # Calculate effort foe this path
                    new_effort = max(effort, abs(heights[new_row][new_col] - heights[row][col]))

                    # If this path is better, update and add to queue
                    if new_effort < min_effort[new_row][new_col]:
                        min_effort[new_row][new_col] = new_effort
                        heapq.heappush(pq, (new_effort, new_row, new_col))

        return 0