# Leetcode 1266: Minimum Time Visiting All Points
# https://leetcode.com/problems/minimum-time-visiting-all-points/
# Solved on 12th of January, 2026
class Solution:
    def minTimeToVisitAllPoints(self, points: list[list[int]]) -> int:
        """
        Calculates the minimum time to visit all points in the given order.
        The movement is restricted to horizontal, vertical, or diagonal moves,
        each taking 1 second.

        :param points: A list of points, where each point is a list [x, y].
        :return: The minimum time to visit all points.
        """
        totalTime = 0

        for i in range(len(points) - 1):
            diffX = abs(points[i + 1][0] - points[i][0])
            diffY = abs(points[i + 1][1] - points[i][1])

            totalTime += max(diffX, diffY)

        return totalTime