# Leetcode 1401: Circle and Rectangle Overlapping
# https://leetcode.com/problems/circle-and-rectangle-overlapping/
# Solved on 19th of September, 2026
class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        """
        Determines whether a circle and an axis-aligned rectangle overlap.

        Parameters:
            radius (int): Radius of the circle.
            xCenter (int): X-coordinate of the circle's center.
            yCenter (int): Y-coordinate of the circle's center.
            x1 (int): X-coordinate of the bottom-left corner of the rectangle.
            y1 (int): Y-coordinate of the bottom-left corner of the rectangle.
            x2 (int): X-coordinate of the top-right corner of the rectangle.
            y2 (int): Y-coordinate of the top-right corner of the rectangle.

        Returns:
            bool: True if the circle and rectangle overlap, False otherwise.
        """
        closestX = max(x1, min(xCenter, x2))
        closestY = max(y1, min(yCenter, y2))
        deltaX = closestX - xCenter
        deltaY = closestY - yCenter
        distanceSquared = deltaX * deltaX + deltaY * deltaY
        radiusSquared = radius * radius
        return distanceSquared <= radiusSquared