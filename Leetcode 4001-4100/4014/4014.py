# Leetcode 4014: Minimum Total Price After Applying Discounts
# https://leetcode.com/problems/minimum-total-price-after-applying-discounts/
# Solved on 6th of September, 2026
class Solution:
    def minPrices(self, prices: list[int], discounts: list[int]) -> float:
        """
        Compute the minimum total price after assigning discounts optimally.

        Args:
            prices (list[int]): The list of original item prices.
            discounts (list[int]): The list of discount percentages.

        Returns:
            float: The minimum possible sum of final item prices.
        """
        prices.sort(reverse=True)
        discounts.sort(reverse=True)

        pairCount = min(len(prices), len(discounts))
        discountedSum = 0
        undiscountedSum = 0

        for itemIndex in range(pairCount):
            discountedSum += prices[itemIndex] * (100 - discounts[itemIndex])

        for itemIndex in range(pairCount, len(prices)):
            undiscountedSum += prices[itemIndex]

        totalPrice = (discountedSum / 100.0) + float(undiscountedSum)
        return totalPrice