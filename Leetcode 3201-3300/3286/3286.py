# Leetcode 3286: Find a Safe Walk Through a Grid
# https://leetcode.com/problems/find-a-safe-walk-through-a-grid/
# Solved on 1st of December, 2025
import collections


class Solution:
    def findSafeWalk(self, grid: list[list[int]], health: int) -> int:
        """
        Finds if there is a safe walk from the top-left to the bottom-right of a grid.

        Args:
            grid: A 2D list of integers representing the cost of moving to each cell.
            health: An integer representing the maximum health allowed to be lost.
        Returns:
            True if a safe walk exists, False otherwise.
        """
        rows = len(grid)
        cols = len(grid[0])
        startCost = grid[0][0]

        if startCost >= health:
            return False

        minHealthLost = [[float('inf')] * cols for _ in range(rows)]
        minHealthLost[0][0] = startCost

        bfsQueue = collections.deque([(0, 0)])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while bfsQueue:
            currRow, currCol = bfsQueue.popleft()

            if currRow == rows - 1 and currCol == cols - 1:
                return True

            currCost = minHealthLost[currRow][currCol]

            for dRow, dCol in directions:
                nextRow, nextCol = currRow + dRow, currCol + dCol

                if 0 <= nextRow < rows and 0 <= nextCol < cols:
                    newCost = currCost + grid[nextRow][nextCol]

                    if newCost < minHealthLost[nextRow][nextCol] and newCost < health:
                        minHealthLost[nextRow][nextCol] = newCost
                        if grid[nextRow][nextCol] == 0:
                            bfsQueue.appendleft((nextRow, nextCol))
                        else:
                            bfsQueue.append((nextRow, nextCol))

        return False