# Leetcode 2249: Count Lattice Points Inside a Circle
# https://leetcode.com/problems/count-lattice-points-inside-a-circle/
# Solved on 8th of November, 2025
class Solution:
    def countLatticePoints(self, circles: list[list[int]]) -> int:
        """
        Counts the total number of unique lattice points that lie inside or on at least one of the given circles.

        Args:
            circles: A list of circles, where each circle is represented as [centerX, centerY, radius].
        Returns:
            The total number of unique lattice points.
        """
        pointSet = set()

        for circleData in circles:
            centerX = circleData[0]
            centerY = circleData[1]
            radius = circleData[2]

            radiusSquared = radius * radius

            for pointX in range(centerX - radius, centerX + radius + 1):
                for pointY in range(centerY - radius, centerY + radius + 1):
                    deltaX = pointX - centerX
                    deltaY = pointY - centerY

                    if (deltaX * deltaX + deltaY * deltaY) <= radiusSquared:
                        pointSet.add((pointX, pointY))

        return len(pointSet)