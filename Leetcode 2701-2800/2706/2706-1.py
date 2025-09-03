# Leetcode 2706: Buy Two Chocolates
# https://leetcode.com/problems/buy-two-chocolates/
# Solved on 3rd of September, 2025
import math


class Solution:
    def buyChoco(self, prices: list[int], money: int) -> int:
        """
        Calculates the remaining money after buying two cheapest chocolates, if affordable.
        :param prices: A list of integers representing the prices of chocolates.
        :param money: An integer representing the initial amount of money.
        :return: An integer representing the remaining money or the initial money if two chocolates cannot be bought.
        """
        firstMin = math.inf
        secondMin = math.inf

        for price in prices:
            if price < firstMin:
                secondMin = firstMin
                firstMin = price
            elif price < secondMin:
                secondMin = price

        minCost = firstMin + secondMin

        if minCost <= money:
            return money - minCost

        return money