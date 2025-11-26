# Leetcode 3625: Count Number of Trapezoids II
# https://leetcode.com/problems/count-number-of-trapezoids-ii/
# Solved on 26th of November, 2025
import math
from collections import defaultdict


class Solution:
    def countTrapezoids(self, points: list[list[int]]) -> int:
        """
        Counts the number of trapezoids formed by a given set of points.

        Args:
            points: A list of lists, where each inner list `[x, y]` represents a point.
        Returns:
            The total number of trapezoids.
        """
        n = len(points)
        slopeMap = defaultdict(lambda: defaultdict(int))
        midMap = defaultdict(lambda: defaultdict(int))

        for i in range(n):
            for j in range(i + 1, n):
                p1 = points[i]
                p2 = points[j]

                dy = p2[1] - p1[1]
                dx = p2[0] - p1[0]
                g = math.gcd(dy, dx)
                dy //= g
                dx //= g

                if dx < 0 or (dx == 0 and dy < 0):
                    dx = -dx
                    dy = -dy

                slope = (dy, dx)
                intercept = dx * p1[1] - dy * p1[0]

                slopeMap[slope][intercept] += 1

                midX = p1[0] + p2[0]
                midY = p1[1] + p2[1]
                midKey = (midX, midY)
                midMap[midKey][slope] += 1

        rawTrapezoidCount = 0
        for slopeData in slopeMap.values():
            counts = list(slopeData.values())
            total = sum(counts)
            sqSum = sum(c * c for c in counts)
            rawTrapezoidCount += (total * total - sqSum) // 2

        parallelogramCount = 0
        for midData in midMap.values():
            slopeCounts = list(midData.values())
            totalPairs = sum(slopeCounts)
            pairsSameSlope = sum(c * (c - 1) // 2 for c in slopeCounts)
            validPairs = (totalPairs * (totalPairs - 1) // 2) - pairsSameSlope
            parallelogramCount += validPairs

        return rawTrapezoidCount - parallelogramCount