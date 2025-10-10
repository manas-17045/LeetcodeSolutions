# Leetcode 2517: Maximum Tastiness of Candy Basket
# https://leetcode.com/problems/maximum-tastiness-of-candy-basket/
# Solved on 10th of October, 2025
class Solution:
    def maximumTastiness(self, price: list[int], k: int) -> int:
        """
        Calculates the maximum possible tastiness such that at least k candies can be chosen.
        :param price: A list of integers representing the prices of candies.
        :param k: An integer representing the number of candies to choose.
        :return: An integer representing the maximum tastiness.
        """
        price.sort()

        def can_achieve(tastiness):
            count = 1
            last = price[0]

            for i in range(1, len(price)):
                if price[i] - last >= tastiness:
                    count += 1
                    last = price[i]
                    if count == k:
                        return True

            return count == k

        # Binary search on the tastiness value
        left, right = 0, (price[-1] - price[0]) // (k - 1)
        result = 0

        while left <= right:
            mid = (left + right) // 2
            if can_achieve(mid):
                result = mid
                left = mid + 1
            else:
                right = mid - 1

        return result