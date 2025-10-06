# Leetcode 1631: Path With Minimum Effort
# https://leetcode.com/problems/path-with-minimum-effort/
# Solved on 6th of October, 2025
import heapq


class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        """
        Finds the minimum effort required to travel from the top-left cell (0, 0)
        to the bottom-right cell (numRows-1, numCols-1) of a 2D grid of heights.
        The effort of a path is the maximum absolute difference in heights between
        any two adjacent cells in the path.
        :param heights: A list of lists of integers representing the heights of cells.
        :return: The minimum effort required to reach the destination.
        """
        numRows = len(heights)
        numCols = len(heights[0])

        minEfforts = [[float('inf')] * numCols for _ in range(numRows)]
        minEfforts[0][0] = 0

        priorityQueue = [(0, 0, 0)]

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while priorityQueue:
            effort, row, col = heapq.heappop(priorityQueue)

            if effort > minEfforts[row][col]:
                continue

            if row == numRows - 1 and col == numCols - 1:
                return effort

            for dRow, dCol in directions:
                newRow = row + dRow
                newCol = col + dCol

                if 0 <= newRow < numRows and 0 <= newCol < numCols:
                    heightDiff = abs(heights[newRow][newCol] - heights[row][col])
                    maxEffort = max(effort, heightDiff)

                    if maxEffort < minEfforts[newRow][newCol]:
                        minEfforts[newRow][newCol] = maxEffort
                        heapq.heappush(priorityQueue, (maxEffort, newRow, newCol))

        return 0