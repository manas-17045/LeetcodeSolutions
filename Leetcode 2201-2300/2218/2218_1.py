# Leetcode 2218: Maximum Value of K Coins From Piles
# https://leetcode.com/problems/maximum-value-of-k-coins-from-piles/
# Solved on 19th of July, 2025
class Solution:
    def maxValueOfCoins(self, piles: list[list[int]], k: int) -> int:
        """
        Calculates the maximum value of k coins that can be picked from the given piles.
        :param piles: A list of lists, where each inner list represents a pile of coins.
        :param k: The maximum number of coins that can be picked.
        :return: The maximum total value of coins that can be obtained.
        """
        dp = [0] * (k + 1)

        for pile in piles:
            prefixSums = []
            currentSum = 0
            for coin in pile:
                currentSum += coin
                prefixSums.append(currentSum)

            for j in range(k, 0, -1):
                pileSize = len(prefixSums)
                for x in range(1, (min(j, pileSize) + 1)):
                    valueFromPile = prefixSums[x - 1]
                    previousValue = dp[j - x]
                    dp[j] = max(dp[j], (previousValue + valueFromPile))

        return dp[k]