# Leetcode 2580: Count Ways to Group Overlapping Ranges
# https://leetcode.com/problems/count-ways-to-group-overlapping-ranges/
# Solved on 1st of September, 2025
class Solution:
    def countWays(self, ranges: list[list[int]]) -> int:
        """
        Counts the number of ways to split a given set of ranges into two groups
        such that no two ranges from the same group overlap.

        Args:
            ranges (list[list[int]]): A list of integer pairs, where each pair [start, end] represents a range.
        Returns:
            int: The number of ways to split the ranges, modulo 10^9 + 7.
        """
        MOD = 10**9 + 7

        # Sort intervals by start
        ranges.sort(key=lambda x: x[0])

        # Count connected components
        components = 0
        curr_end = -1

        for start, end in ranges:
            if start > curr_end:
                # New component starts
                components += 1
                curr_end = end
            else:
                # Merge with current component
                curr_end = max(curr_end, end)

        # Each component has 2 choices (group1 or group2)
        return pow(2, components, MOD)