# Leetcode 3000: Maximum Area of Longest Diagonal Rectangle
# https://leetcode.com/problems/maximum-area-of-longest-diagonal-rectangle/
# Solved on 26th of August, 2025
class Solution:
    def areaOfMaxDiagonal(self, dimensions: list[list[int]]) -> int:
        """
        Calculates the maximum area among rectangles that have the longest diagonal.
        If multiple rectangles have the same longest diagonal, the one with the largest area is chosen.

        Args:
            dimensions (list[list[int]]): A list of lists, where each inner list `[length, width]` represents the dimensions of a rectangle.
        Returns:
            int: The maximum area of the rectangle(s) with the longest diagonal.
        """
        maxDiagonalSquared = 0
        maxArea = 0

        for dimension in dimensions:
            length = dimension[0]
            width = dimension[1]

            currentDiagonalSquared = length * length + width * width

            if currentDiagonalSquared > maxDiagonalSquared:
                maxDiagonalSquared = currentDiagonalSquared
                maxArea = length * width
            elif currentDiagonalSquared == maxDiagonalSquared:
                currentArea = length * width
                if currentArea > maxArea:
                    maxArea = currentArea

        return maxArea