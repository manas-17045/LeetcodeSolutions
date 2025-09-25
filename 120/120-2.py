# Leetcode 120: Triangle
# https://leetcode.com/problems/triangle/
# Solved on 25th of September, 2025
class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        """
        Calculates the minimum path sum from the top to the bottom of a triangle.
        :param triangle: A list of lists of integers representing the triangle.
        :return: The minimum path sum.
        """
        if not triangle:
            return 0

        # dp holds the minimum totals from current row down to bottom
        dp = triangle[-1].copy()

        # Iterate from second-last row up to the top
        for i in range(len(triangle) - 2, -1, -1):
            row = triangle[i]
            # Update dp in-place for this row
            for j in range(len(row)):
                # Choose the smaller of the two adjacent values from the row below
                dp[j] = row[j] + min(dp[j], dp[j + 1])

        return dp[0]