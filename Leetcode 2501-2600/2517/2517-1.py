# Leetcode 2517: Maximum Tastiness of Candy Basket
# https://leetcode.com/problems/maximum-tastiness-of-candy-basket/
# Solved on 10th of October, 2025
class Solution:
    def maximumTastiness(self, price: list[int], k: int) -> int:
        """
        Calculates the maximum tastiness of a candy basket.

        :param price: A list of integers representing the prices of candies.
        :param k: An integer representing the number of candies to select.
        :return: An integer representing the maximum tastiness.
        """
        price.sort()

        def canSelect(minDifference: int) -> bool:
            candiesSelected = 1
            lastPrice = price[0]

            for i in range(1, len(price)):
                if price[i] - lastPrice >= minDifference:
                    candiesSelected += 1
                    lastPrice = price[i]

            return candiesSelected >= k

        low = 0
        high = price[-1] - price[0]
        result = 0

        while low <= high:
            mid = low + (high - low) // 2

            if canSelect(mid):
                result = mid
                low = mid + 1
            else:
                high = mid - 1

        return result