# Leetcode 3652: Best Time to Buy and Sell Stock using Strategy
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-using-strategy/
# Solved on 25th of November, 2025
class Solution:
    def maxProfit(self, prices: list[int], strategy: list[int], k: int) -> int:
        """
        Calculates the maximum profit achievable by buying and selling stocks based on a given strategy
        and the ability to reverse a contiguous subsegment of the strategy.

        Args:
            prices: A list of integers representing the stock prices on consecutive days.
            strategy: A list of integers where strategy[i] is 1 if we buy on day i, and 0 if we sell on day i.
            k: An integer representing the length of the contiguous subsegment of the strategy that can be reversed.
        Returns:
            The maximum profit achievable.
        """
        n = len(prices)
        originalProfit = 0
        for i in range(n):
            originalProfit += strategy[i] * prices[i]

        halfK = k // 2
        currentImprovement = 0

        for i in range(halfK):
            currentImprovement += -strategy[i] * prices[i]

        for i in range(halfK, k):
            currentImprovement += (1 - strategy[i]) * prices[i]

        maxImprovement = max(0, currentImprovement)

        for i in range(n - k):
            currentImprovement -= -strategy[i] * prices[i]

            midIndex = i + halfK
            currentImprovement -= prices[midIndex]

            endIndex = i + k
            currentImprovement += (1 - strategy[endIndex]) * prices[endIndex]

            if currentImprovement > maxImprovement:
                maxImprovement = currentImprovement

        return originalProfit + maxImprovement