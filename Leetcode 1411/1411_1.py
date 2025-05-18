# Leetcode 1411: Number of Ways to Paint N × 3 Grid
# https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid/
# Solved on 18th of May, 2025

class Solution:
    def numOfWays(self, n: int) -> int:
        """
        Calculates the number of ways to paint a 3 × n grid with three colors such that no two adjacent cells have the same color.

        Args:
            n: The number of columns in the grid.

        Returns:
            The number of ways to paint the grid modulo 10^9 + 7.

        """

        MOD = 10**9 + 7

        # Base case for the first row (n = 1)
        # ways_aba: number of ways to color the current row with an ABA pattern
        # ways_abc: number of ways to color the current row with an ABC pattern
        ways_aba = 6
        ways_abc = 6

        if n == 1:
            return (ways_aba + ways_abc) % MOD

        # Iterate for rows from the second row up to the n-th row
        # The loop runs n - 1 times.
        for _ in range(2, n + 1):
            # Calculate ways for the current row based on the previous row's ways

            # Ways to form an ABA pattern in the current row:
            # - Previous row was ABA: prev_ways_aba * 3 (T_ABA_to_ABA)
            # - Previous row was ABC: prev_ways_abc * 2 (T_ABC_to_ABA)
            next_ways_aba = (ways_aba * 3 + ways_abc * 2) % MOD

            # Ways to form an ABC pattern in the current row:
            # - Previous row was ABA: prev_ways_aba * 2 (T_ABA_to_ABC)
            # - Previous row was ABC: prev_ways_abc * 2 (T_ABC_to_ABC)
            next_ways_abc = (ways_aba * 2 + ways_abc * 2) % MOD

            # Update for the next iteration
            ways_aba = next_ways_aba
            ways_abc = next_ways_abc

        return (ways_aba + ways_abc) % MOD