# Leetcode 2267: Check if There Is a Valid Parentheses String Path
# https://leetcode.com/problems/check-if-there-is-a-valid-parentheses-string-path/
# Solved on 24th of August, 2025
class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        """
        Checks if there is a valid parentheses string path from the top-left to the bottom-right of the grid.

        Args:
            grid: A 2D list of strings, where each string is either '(' or ')'.
        Returns:
            True if a valid path exists, False otherwise.
        """
        numRows = len(grid)
        numCols = len(grid[0])

        if (numRows + numCols - 1) % 2 != 0:
            return False

        if grid[0][0] == ')' or grid[numRows - 1][numCols - 1] == '(':
            return False

        memo = {}

        def dfs(row, col, balance):
            if row >= numRows or col >= numCols:
                return False

            if grid[row][col] == '(':
                balance += 1
            else:
                balance -= 1

            remainingCells = (numRows - 1 - row) + (numCols - 1 - col)
            if balance < 0 or balance > remainingCells:
                return False

            if (row, col, balance) in memo:
                return memo[(row, col, balance)]

            if row == numRows - 1 and col == numCols - 1:
                return balance == 0

            pathFound = dfs(row + 1, col, balance) or dfs(row, col + 1, balance)

            memo[(row, col, balance)] = pathFound
            return pathFound

        return dfs(0, 0, 0)