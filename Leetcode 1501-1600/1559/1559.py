# Leetcode 1559: Detect Cycles in 2D Grid
# https://leetcode.com/problems/detect-cycles-in-2d-grid/
# Solved on 26th of April, 2026
from collections import deque


class Solution:
    def containsCycle(self, grid: list[list[str]]) -> bool:
        """
        Detects if there is a cycle of the same value in a 2D grid.
        A cycle must have a length of at least 4 and consist of the same characters.

        :param grid: A 2D list of characters representing the grid.
        :return: True if a cycle exists, False otherwise.
        """
        rowCount = len(grid)
        colCount = len(grid[0])
        visited = [[False] * colCount for _ in range(rowCount)]

        for startRow in range(rowCount):
            for startCol in range(colCount):
                if not visited[startRow][startCol]:
                    targetChar = grid[startRow][startCol]
                    nodeQueue = deque([(startRow, startCol, -1, -1)])
                    visited[startRow][startCol] = True

                    while nodeQueue:
                        currRow, currCol, prevRow, prevCol = nodeQueue.popleft()

                        for rowDir, colDir in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                            newRow = currRow + rowDir
                            newCol = currCol + colDir

                            if 0 <= newRow < rowCount and 0 <= newCol < colCount and grid[newRow][newCol] == targetChar:
                                if not visited[newRow][newCol]:
                                    visited[newRow][newCol] = True
                                    nodeQueue.append((newRow, newCol, currRow, currCol))
                                elif newRow != prevRow or newCol != prevCol:
                                    return True

        return False