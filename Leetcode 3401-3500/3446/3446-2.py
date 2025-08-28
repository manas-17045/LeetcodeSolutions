# Leetcode 3446: Sort Matrix by Diagonals
# https://leetcode.com/problems/sort-matrix-by-diagonals/
# Solved on 28th of August, 2025
class Solution:
    def sortMatrix(self, grid: list[list[int]]) -> list[list[int]]:
        """
        Sorts the elements of a square matrix along its diagonals.
        Diagonals starting from the first row (i.e., where r < c) are sorted in ascending order.
        Diagonals starting from the first column (i.e., where r >= c) are sorted in descending order.

        Args:
            grid (list[list[int]]): A square matrix of integers.

        Returns:
            list[list[int]]: The modified matrix with its diagonals sorted as per the rules.
        """
        n = len(grid)
        if n == 0:
            return grid


        # Helper function to collect, sort and write back a diagonal starting at (r, c)
        def process_diag(r: int, c: int):
            vals = []
            i, j = r, c
            while i < n and j < n:
                vals.append(grid[i][j])
                i += 1
                j += 1

            if r >= c:
                vals.sort(reverse=True)
            else:
                vals.sort()

            # Write back
            i, j = r, c
            k = 0
            while i < n and j < n:
                grid[i][j] = vals[k]
                i += 1
                j += 1
                k += 1

        # Process diagonals starting from the first row
        for c in range(n):
            process_diag(0, c)

        # Process diagonals starting from the first column (skip (0, 0) to avoid duplication)
        for r in range(1, n):
            process_diag(r, 0)

        return grid