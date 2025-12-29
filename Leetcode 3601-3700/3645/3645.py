# Leetcode 3645: Maximum Total from Optimal Activation Order
# https://leetcode.com/problems/maximum-total-from-optimal-activation-order/
# Solved on 29th of December, 2025
from collections import defaultdict


class Solution:
    def maxTotal(self, value: list[int], limit: list[int]) -> int:
        """
        Calculates the maximum total value achievable by optimally activating items.

        Args:
            value: A list of integers representing the value of each item.
            limit: A list of integers representing the activation limit for each item.
        Returns:
            An integer representing the maximum total value.
        """
        limitGroups = defaultdict(list)
        for v, l in zip(value, limit):
            limitGroups[l].append(v)

        totalMax = 0
        for l, group in limitGroups.items():
            group.sort(reverse=True)
            totalMax += sum(group[:l])

        return totalMax