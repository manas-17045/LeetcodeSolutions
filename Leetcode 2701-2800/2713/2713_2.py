# Leetcode 2713: Maximum Strictly Increasing Cells in a Matrix
# https://leetcode.com/problems/maximum-strictly-increasing-cells-in-a-matrix/
# Solved on 8th of July, 2025
class Solution:
    def maxIncreasingCells(self, mat: list[list[int]]) -> int:
        """
        Calculates the maximum length of an increasing path in a given matrix.

        An increasing path can move from a cell (r1, c1) to another cell (r2, c2)
        if mat[r2][c2] > mat[r1][c1] and either r1 == r2 (same row) or c1 == c2 (same column).

        The algorithm sorts all cells by their value and processes them in increasing order.
        For cells with the same value, they are processed as a batch to ensure that
        when calculating the path length for a cell (r, c), the `row_max[r]` and `col_max[c]`
        values reflect paths ending at cells with *smaller* values than mat[r][c].

        Args:
            mat: A list of lists of integers representing the matrix.

        Returns:
            The maximum length of an increasing path found in the matrix.
        """
        m, n = len(mat), len(mat[0])
        # Flatten and sort all cells by value
        cells = []
        for i in range(m):
            for j in range(n):
                cells.append((mat[i][j], i, j))
        cells.sort()

        row_max = [0] * m
        col_max = [0] * n

        ans = 1
        idx = 0
        N = len(cells)

        # Process in batches of equal value
        while idx < N:
            val = cells[idx][0]
            # Collect dp-values for this batch without updating row_max/col_max yet.
            batch = []
            while idx < N and cells[idx][0] == val:
                _, r, c = cells[idx]
                # We can extend the best path in its row or its column.
                dp = max(row_max[r], col_max[c]) + 1
                batch.append((r, c, dp))
                ans = max(ans, dp)
                idx += 1
            # Now, update the row_max and col_max for all cells in the batch
            for r, c, dp in batch:
                if dp > row_max[r]:
                    row_max[r] = dp
                if dp > col_max[c]:
                    col_max[c] = dp

        return ans