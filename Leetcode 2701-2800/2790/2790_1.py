# Leetcode 2790: Maximum Number of Groups With Increasing Length
# https://leetcode.com/problems/maximum-number-of-groups-with-increasing-length/
# Solved on 11th of July, 2025
class Solution:
    def maxIncreasingGroups(self, usageLimits: list[int]) -> int:
        """
        Calculates the maximum number of groups with increasing length that can be formed.

        A group of length `k` requires `k` distinct items.
        Groups must have strictly increasing lengths (e.g., group 1 has length 1, group 2 has length 2, etc.).
        The `usageLimits` array represents the number of available items of each type.

        Args:
            usageLimits: A list of integers representing the count of each item type.

        Returns:
            The maximum number of groups that can be formed.
        """
        usageLimits.sort()

        totalItems = 0
        numGroups = 0

        for limit in usageLimits:
            totalItems += limit

            requiredItems = (numGroups + 1) * (numGroups + 2) // 2

            if totalItems >= requiredItems:
                numGroups += 1

        return numGroups