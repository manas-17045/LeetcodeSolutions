# Leetcode 1453: Maximum Number of Darts Inside of a Circular Dartboard
# https://leetcode.com/problems/maximum-number-of-darts-inside-of-a-circular-dartboard/
# Solved on 3rd of October, 2025
import math


class Solution:
    def numPoints(self, darts: list[list[int]], r: int) -> int:
        """
        Calculates the maximum number of darts that can be contained within a circle of a given radius.

        Args:
            darts: A list of lists, where each inner list represents the [x, y] coordinates of a dart.
            r: The radius of the circle.
        Returns: The maximum number of darts that can be contained within a circle of radius r.
        """
        n = len(darts)
        if n == 1:
            return 1

        max_darts = 1

        # Try circles centered at each dart
        for i in range(n):
            count = sum(1 for j in range(n) if self.distance(darts[i], darts[j]) <= r + 1e-7)
            max_darts = max(max_darts, count)

        # Try circles passing through pairs of darts
        for i in range(n):
            for j in range(i + 1, n):
                dist = self.distance(darts[i], darts[j])

                # If darts are too far apart, no circle of radius r can contain both
                if dist > 2 * r + 1e-7:
                    continue

                # Find centers of circles with radius r passing through both darts
                centers = self.findCircleCenters(darts[i], darts[j], r)

                for center in centers:
                    count = sum(1 for k in range(n) if self.distance(center, darts[k]) <= r + 1e-7)
                    max_darts = max(max_darts, count)

        return max_darts

    def distance(self, p1, p2):
        return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

    def findCircleCenters(self, p1, p2, r):
        x1, y1 = p1
        x2, y2 = p2

        # Midpoint
        mx = (x1 + x2) / 2
        my = (y1 + y2) / 2

        # Distance between points
        dist = self.distance(p1, p2)

        # If points are the same
        if dist < 1e-7:
            return [[x1, y1]]

        # If points are too far apart
        if dist > 2 * r + 1e-7:
            return []

        # Distance from midpoint to circle center
        if dist / 2 > r:
            h = 0
        else:
            h = math.sqrt(r * r - (dist / 2) ** 2)

        # Direction perpendicular to line connecting p1 and p2
        dx = (x2 - x1) / dist
        dy = (y2 - y1) / dist

        # Two possible centers
        c1 = [mx - h * dy, my + h * dx]
        c2 = [mx + h * dy, my - h * dx]

        if h < 1e-7:
            return [c1]

        return [c1, c2]