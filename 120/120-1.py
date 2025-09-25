# Leetcode 120: Triangle
# https://leetcode.com/problems/triangle/
# Solved on 25th of September, 2025
class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        """
        Calculates the minimum path sum from top to bottom of a triangle.

        Args:
            triangle (list[list[int]]): A list of lists representing the triangle.

        Returns:
            int: The minimum path sum.
        """
        numRows = len(triangle)

        for row in range((numRows - 2), -1, -1):
            for col in range(len(triangle[row])):
                minSumBelow = min(triangle[row + 1][col], triangle[row + 1][col + 1])
                triangle[row][col] += minSumBelow

        return triangle[0][0]