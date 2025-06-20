# Leetcode 3567: Minimum Absolute Difference in Sliding Submatrix
# https://leetcode.com/problems/minimum-absolute-difference-in-sliding-submatrix/
# Solved on 20th of June, 2025

class Solution:
    def minAbsDiff(self, grid: list[list[int]], k: int) -> list[list[int]]:
        """
        Calculates the minimum absolute difference between any two distinct elements
        within every k x k subgrid of the given grid.

        For each k x k subgrid, the function finds all unique values, sorts them,
        and then calculates the minimum difference between adjacent elements in the
        sorted list of unique values. If a subgrid contains only one unique value,
        the minimum absolute difference is 0.

        Args:
            grid: A 2D list of integers representing the input grid.
            k: An integer representing the size of the square subgrids.

        Returns:
            A 2D list of integers where each element ans[i][j] represents the
            minimum absolute difference in the k x k subgrid starting at grid[i][j].
        """
        n, m = len(grid), len(grid[0])
        ans = [[0] * (m - k + 1) for _ in range(n - k + 1)]

        for i in range(n - k + 1):
            for j in range(m - k + 1):
                # Collect all values in the k*k block starting at (i, j)
                block = []
                for di in range(k):
                    block.extend(grid[i + di][j:j + k])

                # Dedupe and sort
                vals = sorted(set(block))

                # If only distinct number, diff = 0.
                if len(vals) < 2:
                    ans[i][j] = 0
                else:
                    # Scan adjacent gaps
                    minDiff = float('inf')
                    for x in range(1, len(vals)):
                        d = vals[x] - vals[x - 1]
                        if d < minDiff:
                            minDiff = d
                    ans[i][j] = minDiff

        return ans