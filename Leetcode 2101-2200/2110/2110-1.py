# Leetcode 2210: Number of Smooth Descent Periods of a Stock
# https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock/
# Solved on 7th of September, 2025
class Solution:
    def getDescentPeriods(self, prices: list[int]) -> int:
        """
        Calculates the total number of smooth descent periods in a given list of stock prices.
        A smooth descent period is a contiguous subarray where each element is exactly 1 less than the previous element.

        :param prices: A list of integers representing the stock prices.
        :return: The total number of smooth descent periods.
        """
        numPrices = len(prices)
        count = 0
        streak = 0

        for i in range(numPrices):
            if i > 0 and prices[i - 1] - prices[i] == 1:
                streak += 1
            else:
                streak = 1

            count += streak

        return count