# Leetcode 1895: Largest Magic Square
# https://leetcode.com/problems/largest-magic-square/
# Solved on 18th of January, 2026
class Solution:
    def largestMagicSquare(self, grid: list[list[int]]) -> int:
        """
        Finds the largest magic square within the given grid.

        Args:
            grid: A 2D list of integers representing the grid.
        Returns:
            The side length of the largest magic square found.
        """
        rows = len(grid)
        cols = len(grid[0])
        rowPrefix = [[0] * (cols + 1) for _ in range(rows)]
        colPrefix = [[0] * cols for _ in range(rows + 1)]

        for r in range(rows):
            for c in range(cols):
                rowPrefix[r][c + 1] = rowPrefix[r][c] + grid[r][c]
                colPrefix[r + 1][c] = colPrefix[r][c] + grid[r][c]

        for k in range(min(rows, cols), 1, -1):
            for r in range(rows - k + 1):
                for c in range(cols - k + 1):
                    targetSum = rowPrefix[r][c + k] - rowPrefix[r][c]
                    isValid = True

                    for i in range(k):
                        if rowPrefix[r + i][c + k] - rowPrefix[r + i][c] != targetSum:
                            isValid = False
                            break
                        if colPrefix[r + k][c + i] - colPrefix[r][c + i] != targetSum:
                            isValid = False
                            break

                    if not isValid:
                        continue

                    d1 = 0
                    d2 = 0
                    for i in range(k):
                        d1 += grid[r + i][c + i]
                        d2 += grid[r + i][c + k - 1 - i]

                    if d1 == targetSum and d2 == targetSum:
                        return k

        return 1