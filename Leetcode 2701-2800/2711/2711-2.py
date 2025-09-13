# Leetcode 2711: Difference of Number of Distinct Values on Diagonals
# https://leetcode.com/problems/difference-of-number-of-distinct-values-on-diagonals/
# Solved on 13th of September, 2025
class Solution:
    def differenceOfDistinctValues(self, grid: list[list[int]]) -> list[list[int]]:
        """
        Calculates the difference of distinct values for each cell in a grid based on its diagonal elements.
        :param grid: A 2D list of integers representing the input grid.
        :return: A 2D list of integers where each cell (r, c) contains the absolute difference
                 between the number of distinct values in the top-left diagonal and the bottom-right diagonal.
        """
        m = len(grid)
        n = len(grid[0])
        ans = [[0] * n for _ in range(m)]

        def process_diagonal(sr: int, sc: int) -> None:
            coOrds = []
            vals = []
            r, c = sr, sc
            while r < m and c < n:
                coOrds.append((r, c))
                vals.append(grid[r][c])
                r += 1
                c += 1

            # Prefix distinct counts (left-above)
            seen = set()
            left_counts = []
            for v in vals:
                left_counts.append(len(seen))
                seen.add(v)

            # Suffix distinct counts (right-below) while filling answer
            seen.clear()
            for i in range(len(vals) - 1, -1, -1):
                r, c = coOrds[i]
                right_count = len(seen)
                ans[r][c] = abs(left_counts[i] - right_count)
                seen.add(vals[i])

        # Diagonals starting from top row
        for sc in range(n):
            process_diagonal(0, sc)

        # Diagonals starting from left column (skip the very first since already covered)
        for sr in range(1, m):
            process_diagonal(sr, 0)

        return ans