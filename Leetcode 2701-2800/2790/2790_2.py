# Leetcode 2790: Maximum Number of Groups With Increasing Length
# https://leetcode.com/problems/maximum-number-of-groups-with-increasing-length/
# Solved on 11th of July, 2025
class Solution:
    def maxIncreasingGroups(self, usageLimits: list[int]) -> int:
        """
        Calculates the maximum number of increasing groups that can be formed.

        An increasing group of size `k` requires `k` distinct items, and the total
        usage limit of these `k` items must be at least `k`.
        The goal is to form groups of sizes 1, 2, 3, ..., `G` such that `G` is maximized.

        Args:
            usageLimits: A list of integers representing the usage limits of available items.

        Returns:
            The maximum number of increasing groups that can be formed.
        """
        # Sort the limits, so we always use the smallest budgest first
        usageLimits.sort()

        groups = 0
        need = 1
        available = 0

        for limit in usageLimits:
            available += limit

            if available >= need:
                groups += 1
                available -= need
                need += 1

        return groups