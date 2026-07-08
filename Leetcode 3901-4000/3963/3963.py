# Leetcode 3963: Create Grid With Exactly One Path
# https://leetcode.com/problems/create-grid-with-exactly-one-path/
# Solved on 8th of July, 2026
class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        """
        Creates a grid of size m x n with exactly one path from the top-left cell to
        the bottom-right cell.

        Args:
            m: The number of rows in the grid.
            n: The number of columns in the grid.

        Returns:
            A grid of size m x n with exactly one path from the top-left cell to
            the bottom-right cell.
        """
        firstRow = "." * n
        subsequentRow = "#" * (n - 1) + "."
        ansGrid = [firstRow] + [subsequentRow] * (m - 1)
        return ansGrid