# Leetcode 812: Largest Triangle Area
# https://leetcode.com/problems/largest-triangle-area/
# Solved on 27th of September, 2025
class Solution:
    def largestTriangleArea(self, points: list[list[int]]) -> float:
        """
        Calculates the area of the largest triangle that can be formed from a given list of points.

        Args:
            points: A list of points, where each point is represented as a list [x, y].
        Returns:
            The area of the largest triangle.
        """
        numPoints = len(points)
        maxArea = 0.0

        for i in range(numPoints):
            for j in range(i + 1, numPoints):
                for k in range(j + 1, numPoints):
                    p1 = points[i]
                    p2 = points[j]
                    p3 = points[k]

                    x1, y1 = p1[0], p1[1]
                    x2, y2 = p2[0], p2[1]
                    x3, y3 = p3[0], p3[1]

                    # Shoelace formula to calculate the area of a triangle
                    currentArea = 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))

                    if currentArea > maxArea:
                        maxArea = currentArea

        return maxArea