# Leetcode 1568: Minimum Number of Days to Disconnect Island
# https://leetcode.com/problems/minimum-number-of-days-to-disconnect-island/
# Resolved on 14th of October, 2025
class Solution:
    def minDays(self, grid: list[list[int]]) -> int:
        """
        Given a 2D binary `grid` representing a map of land (1) and water (0),
        return the minimum number of days to disconnect the island.

        Args:
            grid (list[list[int]]): The 2D binary grid representing the map.

        Returns:
            int: The minimum number of days to disconnect the island.
        """

        numRows = len(grid)
        numCols = len(grid[0])

        def countIslands():
            visited = set()
            islandCount = 0
            for r in range(numRows):
                for c in range(numCols):
                    if grid[r][c] == 1 and (r, c) not in visited:
                        islandCount += 1
                        queue = [(r, c)]
                        visited.add((r, c))
                        head = 0
                        while head < len(queue):
                            row, col = queue[head]
                            head += 1

                            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                                nextRow = row + dr
                                nextCol = col + dc

                                if 0 <= nextRow < numRows and 0 <= nextCol < numCols and grid[nextRow][nextCol] == 1 and (nextRow, nextCol) not in visited:
                                    visited.add((nextRow, nextCol))
                                    queue.append((nextRow, nextCol))

            return islandCount

        if countIslands() != 1:
            return 0

        landCells = []
        for r in range(numRows):
            for c in range(numCols):
                if grid[r][c] == 1:
                    landCells.append((r, c))

        for r, c in landCells:
            grid[r][c] = 0
            if countIslands() != 1:
                return 1
            grid[r][c] = 1

        return 2