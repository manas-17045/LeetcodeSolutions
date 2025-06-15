# Leetcode 1289: Minimum Falling Path Sum II
# https://leetcode.com/problems/minimum-falling-path-sum-ii/
# Solved on 15th of June, 2025

class Solution:
    def minFallingPathSum(self, grid: list[list[int]]) -> int:
        """
        Calculates the minimum falling path sum in a square grid where you can move to any cell in the next row
        except for the cell directly below the current cell.

        Args:
            grid: A list of lists of integers representing the square grid.

        Returns:
            The minimum falling path sum.
        """
        n = len(grid)

        # prev_dp[j] will hold the min falling-path sum ending at column j of the previous row
        prev_dp = grid[0][:]

        # Process each subsequent row
        for i in range(1, n):
            # Find the minimum and second minimum in prev_dp, and the index of the minimum
            min1, min2 = float('inf'), float('inf')
            idx1 = -1
            for j, v in enumerate(prev_dp):
                if v < min1:
                    min2 = min1
                    min1 = v
                    idx1 = j
                elif v < min2:
                    min2 = v

            # Build the dp for this row
            curr_dp = [0] * n
            for j in range(n):
                # If the globally smallest came from the same column, we must use the second-smallest
                best_prev = min2 if j == idx1 else min1
                curr_dp[j] = grid[i][j] + best_prev

            prev_dp = curr_dp

        # Answer is the minimum sum ending anywhere in the last row
        return min(prev_dp)