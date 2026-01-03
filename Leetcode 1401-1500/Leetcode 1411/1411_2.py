# Leetcode 1411: Number of Ways to Paint N × 3 Grid
# https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid/
# Solved on 18th of May, 2025

class Solution:
    def numOfWays(self, n: int) -> int:
        """
        Calculates the number of ways to paint an n × 3 grid using three colors (Red, Yellow, Green)
        such that no two adjacent cells have the same color.

        Args:
            n: The number of rows in the grid.

        Returns:
            The number of ways to paint the grid modulo 10^9 + 7.
        """
        MOD = 10**9 + 7

        # dp2 = number of ways where a single row is of "2-color" pattern (ABA)
        # dp3 = number of ways where a single row is of "3-color" pattern (ABC)
        dp2 = 6
        dp3 = 6

        for _ in range(2, n + 1):
            # Transitions derived by counting compatible next-row patterns
            new_dp2 = (dp2 * 3 + dp3 * 2) % MOD
            new_dp3 = (dp2 * 2 + dp3 * 2) % MOD

            # Update for the next iteration
            dp2 = new_dp2
            dp3 = new_dp3

        return (dp2 + dp3) % MOD