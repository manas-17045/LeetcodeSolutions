# Leetcode 1391: Check if There is a Valid Path in a Grid
# https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/
# Solved on 27th of April, 2026
class Solution:
    def hasValidPath(self, grid: list[list[int]]) -> bool:
        """
        Determines if there is a valid path from the top-left cell (0, 0) to the bottom-right cell (m-1, n-1).
        A path is valid if every street in the path is connected to the next street.

        :param grid: A 2D grid of integers representing different street types.
        :return: True if a valid path exists, False otherwise.
        """
        numRows = len(grid)
        numCols = len(grid[0])

        streetDirs = {
            1: [(0, -1), (0, 1)],
            2: [(-1, 0), (1, 0)],
            3: [(0, -1), (1, 0)],
            4: [(0, 1), (1, 0)],
            5: [(0, -1), (-1, 0)],
            6: [(0, 1), (-1, 0)]
        }

        visitedCells = set()
        visitedCells.add((0, 0))
        stackCells = [(0, 0)]

        while stackCells:
            currRow, currCol = stackCells.pop()

            if currRow == numRows - 1 and currCol == numCols - 1:
                return True

            for deltaRow, deltaCol in streetDirs[grid[currRow][currCol]]:
                nextRow = currRow + deltaRow
                nextCol = currCol + deltaCol

                if 0 <= nextRow < numRows and 0 <= nextCol < numCols and (nextRow, nextCol) not in visitedCells:
                    if (-deltaRow, -deltaCol) in streetDirs[grid[nextRow][nextCol]]:
                        visitedCells.add((nextRow, nextCol))
                        stackCells.append((nextRow, nextCol))

        return False