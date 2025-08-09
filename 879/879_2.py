# Leetcode 879: Profitable Schemes
# https://leetcode.com/problems/profitable-schemes/
# Solved on 9th of August, 2025
class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: list[int], profit: list[int]) -> int:
        """
        Calculates the number of profitable schemes that can be formed.

        Args:
            n (int): The maximum number of members allowed in a scheme.
            minProfit (int): The minimum profit required for a scheme to be considered profitable.
            group (list[int]): A list where group[i] is the number of members required for the i-th crime.
            profit (list[int]): A list where profit[i] is the profit gained from the i-th crime.
        Returns:
            int: The total number of profitable schemes modulo 10^9 + 7.
        """
        MOD = 10**9 + 7
        P = minProfit
        # dp[p][m] = number of schemes that achieve profit p (capped at P) using m members
        dp = [[0] * (n + 1) for _ in range(P + 1)]
        dp[0][0] = 1

        for g, prof in zip(group, profit):
            # Iterate members and profit downward to avoid reusing the current crime multiple times
            for members in range(n, g - 1, -1):
                for p in range(P, -1, -1):
                    newP = p + prof
                    if newP > P:
                        newP = P
                    dp[newP][members] = (dp[newP][members] + dp[p][members - g]) % MOD

        # Sum all schemes that have profit >= minProfit with members <= n
        return sum(dp[P][m] for m in range(n + 1)) % MOD