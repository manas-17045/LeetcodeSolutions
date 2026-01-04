# Leetcode 3070: Count Submatrices with Top-Left Element and Sum Less Than k
# https://leetcode.com/problems/count-submatrices-with-top-left-element-and-sum-less-than-k/
# Solved on 4th of January, 2026
class Solution:
    def countSubmatrices(self, grid: list[list[int]], k: int) -> int:
        """
        Counts the number of submatrices with their top-left element at (0,0)
        and a sum less than or equal to k.

        The function modifies the input `grid` in-place to store prefix sums.
        `grid[r][c]` will store the sum of the submatrix from (0,0) to (r,c).

        Args:
            grid (list[list[int]]): The input 2D integer grid.
            k (int): The maximum allowed sum for a submatrix.

        Returns:
            int: The total count of such submatrices.
        """
        rows = len(grid)
        cols = len(grid[0])

        count = 0
        for r in range(rows):
            for c in range(cols):
                if r > 0:
                    grid[r][c] += grid[r - 1][c]
                if c > 0:
                    grid[r][c] += grid[r][c - 1]
                if r > 0 and c > 0:
                    grid[r][c] -= grid[r - 1][c - 1]

                if grid[r][c] <= k:
                    count += 1
                else:
                    break

        return count