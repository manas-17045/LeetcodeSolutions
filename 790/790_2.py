# Leetcode 790: Domino and Tromino Tiling
# https://leetcode.com/problems/domino-and-tromino-tiling/

class Solution:
    def numTilings(self, n: int) -> int:
        """
        Calculates the number of ways to tile a 2 x n board using 1 x 2 dominoes and 2 x 2 trominoes.
        The calculation uses dynamic programming to compute the result efficiently, accounting for
        modulo 10**9 + 7 to prevent overflow of large numbers. It optimizes space complexity by
        storing only necessary intermediate results during the computation.

        :param n: The length of the board to be tiled
        :type n: int
        :return: The number of ways to tile the board modulo 10**9 + 7
        :rtype: int
        """
        MOD = 10**9 + 7

        if n <= 2:
            return 1 if n == 1 else 2

        # Only maintain the last few values we need
        dp_i_minus_2 = 1    # dp[i - 2]
        dp_i_minus_1 = 2    # dp[i - 1]
        p_i_minus_1 = 1    # p[i - 1]

        for i in range(3, n + 1):
            dp_i = (dp_i_minus_1 + dp_i_minus_2 + 2 * p_i_minus_1) % MOD
            p_i = (dp_i_minus_2 + p_i_minus_1) % MOD

            dp_i_minus_2 = dp_i_minus_1
            dp_i_minus_1 = dp_i
            p_i_minus_1 = p_i

        return dp_i_minus_1