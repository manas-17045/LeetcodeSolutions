# Leetcode 2167: Minimum Time to Remove All Cars Containing Illegal Goods
# https://leetcode.com/problems/minimum-time-to-remove-all-cars-containing-illegal-goods/
# Solved on 27th of November, 2025
class Solution:
    def minimumTime(self, s: str) -> int:
        """
        Calculates the minimum time to remove all cars containing illegal goods.

        The problem can be solved using a dynamic programming approach.
        For each car, we consider the cost of removing it from the left side.

        Args:
            s (str): A binary string representing the cars, where '1' means illegal goods.
        Returns:
            int: The minimum time required to remove all cars with illegal goods.
        """
        n = len(s)
        minTotal = n
        leftCost = 0

        for i, char in enumerate(s):
            if char == '1':
                leftCost = min(leftCost + 2, i + 1)
            minTotal = min(minTotal, leftCost + n - 1 - i)

        return minTotal