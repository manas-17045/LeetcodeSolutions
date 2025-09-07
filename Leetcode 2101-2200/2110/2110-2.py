# Leetcode 2210: Number of Smooth Descent Periods of a Stock
# https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock/
# Solved on 7th of September, 2025
class Solution:
    def getDescentPeriods(self, prices: list[int]) -> int:
        """
        Calculates the total number of smooth descent periods in a given array of stock prices.

        Args:
            prices (list[int]): A list of integers representing stock prices.
        Returns:
            int: The total number of smooth descent periods.
        """
        n = len(prices)
        total = 0
        # Length of current smooth descent period
        curr_len = 0

        for i in range(n):
            if i > 0 and prices[i - 1] - prices[i] == 1:
                curr_len += 1
            else:
                curr_len = 1

            total += curr_len

        return total