# Leetcode 2218: Maximum Value of K Coins From Piles
# https://leetcode.com/problems/maximum-value-of-k-coins-from-piles/
# Solved on 19th of July, 2025
class Solution:
    def maxValueOfCoins(self, piles: list[list[int]], k: int) -> int:
        """
        Calculates the maximum value of coins that can be collected from a set of piles,
        given a maximum number of coins `k` that can be taken.

        Args:
            piles (list[list[int]]): A list of lists, where each inner list represents a pile of coins.
            k (int): The maximum number of coins that can be taken in total.

        Returns:
            int: The maximum value of coins that can be collected.
        """
        dp = [0] * (k + 1)

        for pile in piles:
            m = len(pile)
            prefix = [0] * (m + 1)
            for i in range(m):
                prefix[i + 1] = prefix[i] + pile[i]

            prev_dp = dp[:]
            for j in range(1, k + 1):
                best = prev_dp[j]
                max_take = min(j, m)
                for x in range(1, (max_take + 1)):
                    candidate = prev_dp[j - x] + prefix[x]
                    if candidate > best:
                        best = candidate
                dp[j] = best

        return dp[k]