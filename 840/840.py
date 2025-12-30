# Leetcode 840: Magic Squares In Grid
# https://leetcode.com/problems/magic-squares-in-grid/
# Solved on 30th of December, 2025
class Solution:
    def numMagicSquaresInside(self, grid: list[list[int]]) -> int:
        """
        Calculates the number of 3x3 magic squares present in the given grid.

        Args:
            grid (list[list[int]]): The input grid of integers.
        Returns:
            int: The number of 3x3 magic squares found in the grid.
        """
        numRows = len(grid)
        numCols = len(grid[0])
        count = 0

        for r in range(numRows - 2):
            for c in range(numCols - 2):
                if grid[r + 1][c + 1] != 5:
                    continue

                subGrid = [
                    grid[r][c], grid[r][c + 1], grid[r][c + 2],
                    grid[r + 1][c], grid[r + 1][c + 1], grid[r + 1][c + 2],
                    grid[r + 2][c], grid[r + 2][c + 1], grid[r + 2][c + 2]
                ]

                if sorted(subGrid) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                    continue

                row1 = subGrid[0] + subGrid[1] + subGrid[2]
                row2 = subGrid[3] + subGrid[4] + subGrid[5]
                row3 = subGrid[6] + subGrid[7] + subGrid[8]

                col1 = subGrid[0] + subGrid[3] + subGrid[6]
                col2 = subGrid[1] + subGrid[4] + subGrid[7]
                col3 = subGrid[2] + subGrid[5] + subGrid[8]

                diag1 = subGrid[0] + subGrid[4] + subGrid[8]
                diag2 = subGrid[2] + subGrid[4] + subGrid[6]

                if (row1 == 15 and row2 == 15 and row3 == 15 and
                        col1 == 15 and col2 == 15 and col3 == 15 and
                        diag1 == 15 and diag2 == 15):
                    count += 1

        return count