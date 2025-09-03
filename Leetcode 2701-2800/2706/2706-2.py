# Leetcode 2706: Buy Two Chocolates
# https://leetcode.com/problems/buy-two-chocolates/
# Solved on 3rd of September, 2025
class Solution:
    def buyChoco(self, prices: list[int], money: int) -> int:
        """
        Determines the amount of money left after buying two chocolates, given their prices and initial money.
        :param prices: A list of integers representing the prices of available chocolates.
        :param money: An integer representing the initial amount of money.
        :return: An integer representing the money left after buying two cheapest chocolates, or the original money if not enough.
        """
        # Find the two smallest prices
        first = float('inf')
        second = float('inf')
        for p in prices:
            if p < first:
                second = first
                first = p
            elif p < second:
                second = p

        # If we can buy both, return leftover; otherwise return original money
        if first + second <= money:
            return money - (first + second)

        return money