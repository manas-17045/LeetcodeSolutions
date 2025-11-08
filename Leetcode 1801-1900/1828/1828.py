# Leetcode 1828: Queries on Number of Points Inside a Circle
# https://leetcode.com/problems/queries-on-number-of-points-inside-a-circle/
# Solved on 8th of November, 2025
class Solution:
    def countPoints(self, points: list[list[int]], queries: list[list[int]]) -> list[int]:
        """
        Calculates the number of points that lie inside or on the boundary of each given circle.

        Args:
            points: A list of points, where each point is represented as [x, y].
            queries: A list of queries, where each query is represented as [centerX, centerY, radius].

        Returns:
            A list of integers, where each integer is the count of points inside the corresponding circle.
        """
        result = []

        for query in queries:
            centerX = query[0]
            centerY = query[1]
            radius = query[2]

            count = 0
            radiusSquared = radius * radius

            for point in points:
                pointX = point[0]
                pointY = point[1]

                deltaX = pointX - centerX
                deltaY = pointY - centerY

                distSquared = (deltaX * deltaX) + (deltaY * deltaY)

                if distSquared <= radiusSquared:
                    count += 1

            result.append(count)

        return result