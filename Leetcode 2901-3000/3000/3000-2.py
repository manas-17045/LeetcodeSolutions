# Leetcode 3000: Maximum Area of Longest Diagonal Rectangle
# https://leetcode.com/problems/maximum-area-of-longest-diagonal-rectangle/
# Solved on 26th of August, 2025
class Solution:
    def areaOfMaxDiagonal(self, dimensions: list[list[int]]) -> int:
        """
        Calculates the area of the rectangle with the largest diagonal. If multiple rectangles have the same largest diagonal,
        it returns the area of the one with the largest area among them.
        :param dimensions: A list of lists, where each inner list [l, w] represents the length and width of a rectangle.
        :return: The area of the rectangle that satisfies the criteria.
        """
        # Store squared diagonal to avoid sqrt and floating error
        max_sq_diag = -1
        max_area = 0

        for l, w in dimensions:
            sq = l * l + w * w
            area = l * w
            if sq > max_sq_diag:
                max_sq_diag = sq
                max_area = area
            elif sq == max_sq_diag and area > max_area:
                max_area = area

        return max_area