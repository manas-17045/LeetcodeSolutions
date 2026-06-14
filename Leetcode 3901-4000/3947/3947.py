# Leetcode 3947: Maximum Number of Items From Sale II
# https://leetcode.com/problems/maximum-number-of-items-from-sale-ii/
# Solved on 14th of June, 2026
class Solution:
    def maximumSaleItems(self, items: list[list[int]], budget: int) -> int:
        """
        Calculates the maximum number of items that can be purchased within a given budget,
        considering item factors and price-based gains.

        :param items: A list of lists where each sublist contains [factor, price].
        :param budget: The total available budget as an integer.
        :return: The maximum number of items that can be obtained as an integer.
        """
        numItems = len(items)
        freq = [0] * (numItems + 1)
        for factor, price in items:
            freq[factor] += 1

        multiplesCount = [0] * (numItems + 1)
        for f in range(1, numItems + 1):
            if freq[f] > 0:
                for m in range(f, numItems + 1, f):
                    multiplesCount[m] += freq[m]

        minPrice = min(price for factor, price in items)

        validItems = []
        for factor, price in items:
            gain = multiplesCount[factor] - 1
            if price < 2 * minPrice and gain > 0:
                validItems.append((price, gain))

        validItems.sort(key=lambda x: x[0])

        totalItems = 0
        for price, gain in validItems:
            if budget <= 0:
                break
            purchaseAmount = min(gain, budget // price)
            totalItems += 2 * purchaseAmount
            budget -= purchaseAmount * price

        totalItems += budget // minPrice
        return totalItems