# Leetcode 3573: Best Time to Buy and Sell Stock V
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Solved on 16th of June, 2025

class Solution:
    def maximumProfits(self, prices: list[int], k: int) -> int:
        """
        Calculates the maximum profit achievable with at most k transactions.

        A transaction consists of buying and selling a stock. We can also short
        sell, which means selling first and buying later.

        Args:
            prices: A list of integers representing the stock prices on consecutive days.
            k: The maximum number of transactions allowed.

        Returns:
            The maximum profit achievable.
        """
        n = len(prices)

        if n < 2 or k == 0:
            return 0

        # dp arrays sized (k + 1)
        free = [float('-inf')] * (k + 1)
        long = [float('-inf')] * (k + 1)
        short = [float('-inf')] * (k + 1)

        # Start with zero completed, no position
        free[0] = 0

        for p in prices:
            prev_free = free[:]
            prev_long = long[:]
            prev_short = short[:]

            # Opening a long or short does NOT yet increment completed count
            for t in range(k + 1):
                # Open long at price p
                long[t] = max(prev_long[t], prev_free[t] - p)
                # Open short at price p (sell first)
                short[t] = max(prev_short[t], prev_long[t] + p)

            # Closing long/short DOES increment the transaction count
            # So free[t] may come from prev_long[t-1] + p  or prev_short[t-1] - p
            # for t>=1.  free[0] stays as prev_free[0].
            for t in range(1, k + 1):
                free[t] = max(
                    prev_free[t],
                    prev_long[t - 1] + p,
                    prev_short[t - 1] - p
                )
            # free[0] carries over
            free[0] = prev_free[0]

        # We may not need to use all k transactions
        return int(max(free))