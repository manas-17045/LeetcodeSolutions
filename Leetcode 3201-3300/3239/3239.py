# Leetcode 3239: Minimum Number of Flips to Make Binary Grid Palindromic I
# https://leetcode.com/problems/minimum-number-of-flips-to-make-binary-grid-palindromic-i/
# Solved on 2nd of July, 2025
class Solution:
    def minFlips(self, grid: list[list[int]]) -> int:
        """
        Calculates the minimum number of flips required to make the binary grid palindromic.

        A grid can be made palindromic either by making each row palindromic or by making each column palindromic.
        This function calculates the flips needed for both scenarios and returns the minimum of the two.

        Args:
            grid: A list of lists of integers representing the binary grid.
        Returns:
            The minimum number of flips required.
        """
        numRows = len(grid)
        numCols = len(grid[0])

        rowFlips = 0
        for i in range(numRows):
            for j in range(numCols // 2):
                if grid[i][j] != grid[i][numCols - 1 - j]:
                    rowFlips += 1

        colFlips = 0
        for j in range(numCols):
            for i in range(numRows // 2):
                if grid[i][j] != grid[numRows - 1 - i][j]:
                    colFlips += 1

        return min(rowFlips, colFlips)