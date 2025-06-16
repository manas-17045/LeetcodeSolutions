# Leetcode 3573: Best Time to Buy and Sell Stock V
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Solved on 16th of June, 2025
import math


class Solution:
    def maximumProfits(self, prices: list[int], k: int) -> int:
        """
        Calculates the maximum profit that can be achieved by buying and selling stock at most k times.

        Args:
            prices: A list of integers representing the price of the stock on each day.
            k: The maximum number of transactions allowed.

        Returns:
            The maximum profit that can be achieved.
        """
        n = len(prices)
        if n < 2:
            return 0

        prevDp = [0] * n

        for j in range(1, (k + 1)):
            currentDp = [0] * n
            maxVal1 = -math.inf
            maxVal2 = -math.inf

            for i in range(1, n):
                prevProfit = prevDp[i - 2] if i > 1 else 0
                maxVal1 = max(maxVal1, (prevProfit - prices[i - 1]))
                maxVal2 = max(maxVal2, (prevProfit + prices[i - 1]))

                profitNoTxn = currentDp[i - 1]
                profitWithTxn = max((prices[i] + maxVal1), (maxVal2 - prices[i]))

                currentDp[i] = max(profitNoTxn, profitWithTxn)

            prevDp = currentDp

        return prevDp[n - 1]