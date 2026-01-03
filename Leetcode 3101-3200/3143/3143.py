# Leetcode 3143: Maximum Points Inside the Square
# https://leetcode.com/problems/maximum-points-inside-the-square/
# Solved on 3rd of January, 2026
class Solution:
    def maxPointsInsideSquare(self, points: list[list[int]], s: str) -> int:
        """
        Calculates the maximum number of points that can be inside a square centered at (0,0).

        Args:
            points: A list of [x, y] coordinates for each point.
            s: A string where s[i] is the tag of the i-th point.
        Returns:
            The maximum number of points that can be inside the square.
        """
        minDist = {}
        limit = float('inf')

        for point, tag in zip(points, s):
            dist = max(abs(point[0]), abs(point[1]))

            if tag not in minDist:
                minDist[tag] = dist
            elif dist < minDist[tag]:
                limit = min(limit, minDist[tag])
                minDist[tag] = dist
            else:
                limit = min(limit, dist)

        count = 0
        for point in points:
            if max(abs(point[0]), abs(point[1])) < limit:
                count += 1

        return count