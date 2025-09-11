# Leetcode 3393: Count Paths With the Given XOR Value
# https://leetcode.com/problems/count-paths-with-the-given-xor-value/
# Solved on 11th of September, 2025
class Solution:
    def countPathsWithXorValue(self, grid: list[list[int]], k: int) -> int:
        """
        Counts the number of paths from (0,0) to (rows-1, cols-1) in a grid such that the XOR sum of all
        elements along the path equals k.

        :param grid: A 2D list of integers representing the grid.
        :param k: The target XOR sum.
        :return: The number of paths with the given XOR value, modulo 10^9 + 7.
        """
        rows = len(grid)
        cols = len(grid[0])
        mod = 10**9 + 7

        dp = [[[0] * 16 for _ in range(cols)] for _ in range(rows)]
        dp[0][0][grid[0][0]] = 1

        for row in range(rows):
            for col in range(cols):
                if row == 0 and col == 0:
                    continue

                currentValue = grid[row][col]

                for currentXor in range(16):
                    prevXor = currentXor ^ currentValue

                    fromTop = 0
                    if row > 0:
                        fromTop = dp[row - 1][col][prevXor]

                    fromLeft = 0
                    if col > 0:
                        fromLeft = dp[row][col - 1][prevXor]

                    dp[row][col][currentXor] = (fromTop + fromLeft) % mod

        return dp[rows - 1][cols - 1][k]