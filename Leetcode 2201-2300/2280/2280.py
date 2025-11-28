# Leetcode 2280: Minimum Lines to Represent a Line Chart
# https://leetcode.com/problems/minimum-lines-to-represent-a-line-chart/
# Solved on 28th of November, 2025
class Solution:
    def minimumLines(self, stockPrices: list[list[int]]) -> int:
        """
        Calculates the minimum number of lines required to represent a line chart
        given a list of stock prices.

        Args:
            stockPrices (list[list[int]]): A list of stock prices, where each inner list
                                           represents [day, price].
        Returns:
            int: The minimum number of lines needed.
        """
        totalPoints = len(stockPrices)
        if totalPoints < 2:
            return 0

        stockPrices.sort(key=lambda point: point[0])

        lineCount = 1
        previousDiffY = stockPrices[1][1] - stockPrices[0][1]
        previousDiffX = stockPrices[1][0] - stockPrices[0][0]

        for i in range(2, totalPoints):
            currentDiffY = stockPrices[i][1] - stockPrices[i - 1][1]
            currentDiffX = stockPrices[i][0] - stockPrices[i - 1][0]

            if previousDiffY * currentDiffX != currentDiffY * previousDiffX:
                lineCount += 1
                previousDiffY = currentDiffY
                previousDiffX = currentDiffX

        return lineCount