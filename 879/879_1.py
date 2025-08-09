# Leetcode 879: Profitable Schemes
# https://leetcode.com/problems/profitable-schemes/
# Solved on 9th of August, 2025
class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: list[int], profit: list[int]) -> int:
        """
        Calculates the number of profitable schemes that can be formed.

        Args:
            n (int): The maximum number of members available.
            minProfit (int): The minimum profit required for a scheme to be considered profitable.
            group (list[int]): A list where group[i] is the number of members required for the i-th crime.
            profit (list[int]): A list where profit[i] is the profit gained from the i-th crime.

        Returns:
            int: The total number of profitable schemes modulo 10^9 + 7.
        """

        dp = [[0] * (n + 1) for _ in range(minProfit + 1)]
        dp[0][0] = 1
        mod = 10 ** 9 + 7

        for crimeProfit, membersRequired in zip(profit, group):
            for currentMembers in range(n, membersRequired - 1, -1):
                for currentProfit in range(minProfit, -1, -1):
                    newProfit = min(minProfit, currentProfit + crimeProfit)
                    schemesBefore = dp[currentProfit][currentMembers - membersRequired]
                    dp[newProfit][currentMembers] = (dp[newProfit][currentMembers] + schemesBefore) % mod

        totalProfitableSchemes = sum(dp[minProfit]) % mod
        return totalProfitableSchemes