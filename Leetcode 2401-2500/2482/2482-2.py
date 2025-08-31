# Leetcode 2482: Difference Between Ones and Zeros in Row and Column
# https://leetcode.com/problems/difference-between-ones-and-zeros-in-row-and-column/
# Solved on 31st of August, 2025
class Solution:
    def onesMinusZeros(self, grid: list[list[int]]) -> list[list[int]]:
        """
        Calculates the difference matrix where each element diff[i][j] is
        the number of ones in row i plus the number of ones in column j,
        minus the number of zeros in row i minus the number of zeros in column j.
        :param grid: A 2D list of integers (0s and 1s).
        :return: A 2D list of integers representing the difference matrix.
        """
        m = len(grid)
        if m == 0:
            return []

        n = len(grid[0])

        # Ones per row
        ones_row = [sum(row) for row in grid]
        # Ones per column
        ones_col = [sum(col) for col in zip(*grid)]

        # Build result using the derived formula:
        # diff[i][j] = 2 * ones_row[i] + 2 * ones_col[j] - n - m
        res = [[0] * n for _ in range(m)]
        base = -(n + m)
        for i in range(m):
            ri = 2 * ones_row[i]
            row_res = res[i]
            for j in range(n):
                row_res[j] = ri + 2 * ones_col[j] + base

        return res