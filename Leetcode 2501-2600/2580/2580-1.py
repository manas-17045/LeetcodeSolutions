# Leetcode 2580: Count Ways to Group Overlapping Ranges
# https://leetcode.com/problems/count-ways-to-group-overlapping-ranges/
# Solved on 1st of September, 2025
class Solution:
    def countWays(self, ranges: list[list[int]]) -> int:
        """
        Counts the number of ways to group overlapping ranges.

        Args:
            ranges: A list of integer pairs representing the ranges.
        Returns:
            The number of ways to group the ranges, modulo 1,000,000,007.
        """
        modulo = 1_000_000_007
        ranges.sort()

        numberOfComponents = 0
        currentEnd = -1

        for start, end in ranges:
            if start > currentEnd:
                numberOfComponents += 1
                currentEnd = end
            else:
                currentEnd = max(currentEnd, end)

        return pow(2, numberOfComponents, modulo)