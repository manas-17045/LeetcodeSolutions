# Leetcode 3111: Minimum Rectangles to Cover Points
# https://leetcode.com/problems/minimum-rectangles-to-cover-points/
# Solved on 4th of January, 2026
class Solution:
    def minRectanglesToCoverPoints(self, points: list[list[int]], w: int) -> int:
        """
        Calculates the minimum number of rectangles of width 'w' required to cover all given points.

        Args:
            points: A list of [x, y] coordinates representing the points.
            w: The width of each rectangle.
        Returns:
            The minimum number of rectangles required.
        """
        points.sort(key=lambda x: x[0])

        rectangleCount = 0
        currentLimit = -1
        for point in points:
            if point[0] > currentLimit:
                rectangleCount += 1
                currentLimit = point[0] + w

        return rectangleCount