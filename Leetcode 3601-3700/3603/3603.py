# Leetcode 3603: Minimum Cost Path with Alternating Directions II
# https://leetcode.com/problems/minimum-cost-path-with-alternating-directions-ii/
# Solved on 23rd of November, 2025
class Solution:
    def minCost(self, m: int, n: int, waitCost: list[list[int]]) -> int:
        """
        Calculates the minimum cost to reach the bottom-right cell (m-1, n-1)
        from the top-left cell (0, 0) in a grid, with alternating direction costs.

        Args:
            m (int): The number of rows in the grid.
            n (int): The number of columns in the grid.
            waitCost (list[list[int]]): A 2D list representing the waiting cost at each cell.

        Returns:
            int: The minimum cost to reach the bottom-right cell.
        """
        waitCost[0][0] = 0
        dp = [0] * n
        dp[0] = 1

        for j in range(1, n):
            dp[j] = dp[j - 1] + waitCost[0][j - 1] + (j + 1)

        for i in range(1, m):
            dp[0] += waitCost[i - 1][0] + (i + 1)
            for j in range(1, n):
                entryCost = (i + 1) * (j + 1)
                fromTop = dp[j] + waitCost[i - 1][j] + entryCost
                fromLeft = dp[j - 1] + waitCost[i][j - 1] + entryCost
                if fromTop < fromLeft:
                    dp[j] = fromTop
                else:
                    dp[j] = fromLeft

        return dp[n - 1]