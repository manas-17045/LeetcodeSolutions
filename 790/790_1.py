# Leetcode 790: Domino and Tromino Tiling
# https://leetcode.com/problems/domino-and-tromino-tiling/

class Solution:
    def numTilings(self, n: int) -> int:
        """
        Calculates the number of ways to tile a 2 x n board using dominoes (1 x 2 or 2 x 1)
        or trominoes (L-shaped pieces made up of three squares). The result is computed
        modulo 1,000,000,007 (10^9 + 7). The function leverages dynamic programming where
        only the states for the previous two columns and the previous partial tiling states
        are maintained for efficiency.

        :param n: The size of the board to be tiled, where n is the number of columns in
            a 2 x n board.
        :type n: int
        :return: The number of ways to completely tile the 2 x n board, modulo
            1,000,000,007.
        :rtype: int
        """
        MOD = 1_000_000_007

        # Base cases handle small values of n directly.
        # The problem statement implies n >= 1, but dp relation works with n = 0.
        if n == 0:
            return 1    # One way to tile a 2x0 board (do nothing)
        if n == 1:
            return 1    # One way for 2x1 (one vertical domino)
        if n == 2:
            return 2    # Two ways for 2x2 (two vertical or two horizontal dominoes)

        # --- Dynamic Programming State variables ---
        # We only need the states for the previous two columns (i-1 and i-2)
        # to calculate the state for the current column (i).

        # dp2 represents dp[i-2]: Number of ways to fully tile a 2x(i-2) board.
        # Initialize based on i = 3 calculation needs: dp2 = dp[1]
        dp2 = 1

        # dp1 represents dp[i-1]: Number of ways to fully tile a 2x(i-1) board.
        # Initialize based on i = 3 calculation needs: dp1 = dp[2]
        dp1 = 2

        # p1 represents partial[i - 1]: Number of ways to tile a 2x(i-1) board
        # leaving one specific cell (e.g., top) in column i - 1 uncovered.
        # Initialize based on i = 3 calculation needs: p1 = partial[2]
        # partial[2] = (dp[0] + partial[1]) % MOD = (1 + 0) % MOD = 1
        p1 = 1

        # --- DP calculation loop ---
        # Iterate from column i = 3 up to n.
        # In each iteration, calculate dp[i] and partial[i] using dp[i - 1], dp[i -2], partial[i - 1].
        for i in range(3, n + 1):
            # Calculate dp[i] using the recurrence:
            # dp[i] = (dp[i - 1] + dp[i - 2] + 2 * partial[i - 1]) % MOD
            dp_i = (dp1 + dp2 + 2 * p1) % MOD

            # Calculate partial[i] using the recurrence:
            # partial[i] = (dp[i - 2] + partial[i - 1]) % MOD
            p_i = (dp2 + p1) % MOD

            # --- Update states for the next iteration (i + 1) ---
            # The current dp1 becomes the next dp2
            dp2 = dp1
            # The current p_i becomes the next p1
            p1 = p_i
            # The current dp1 becomes the next dp1
            dp1 = dp_i

        # After the loop finishes (i = n), dp1 holds the value for dp[n].
        return dp1