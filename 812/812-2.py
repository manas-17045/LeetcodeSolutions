# Leetcode 812: Largest Triangle Area
# https://leetcode.com/problems/largest-triangle-area/
# Solved on 27th of September, 2025
import itertools


class Solution:
    def largestTriangleArea(self, points: list[list[int]]) -> float:
        """
        Calculates the area of the largest triangle that can be formed from a given list of points.

        :param points: A list of points, where each point is represented as a list [x, y].
        :return: The area of the largest triangle.
        """
        max_double_area = 0
        for (x1, y1), (x2, y2), (x3, y3) in itertools.combinations(points, 3):
            double_area = abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
            if double_area > max_double_area:
                max_double_area = double_area

        return max_double_area / 2.0