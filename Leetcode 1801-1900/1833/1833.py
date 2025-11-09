# Leetcode 1833: Maximum Ice Cream Bars
# https://leetcode.com/problems/maximum-ice-cream-bars/
# Solved on 9th of September, 2025
class Solution:
    def maxIceCream(self, costs: list[int], coins: int) -> int:
        """
        Calculates the maximum number of ice cream bars that can be bought given their costs and available coins.

        :param costs: A list of integers representing the cost of each ice cream bar.
        :param coins: An integer representing the total coins available.
        :return: An integer representing the maximum number of ice cream bars that can be bought.
        """
        barsBought = 0
        currentCoins = coins

        maxCostValue = 100000
        costFrequency = [0] * (maxCostValue + 1)

        for price in costs:
            costFrequency[price] += 1

        for cost in range(1, maxCostValue + 1):
            if currentCoins < cost:
                break

            numBars = costFrequency[cost]
            if numBars == 0:
                continue

            buyCount = min(numBars, currentCoins // cost)
            currentCoins -= buyCount * cost
            barsBought += buyCount

        return barsBought