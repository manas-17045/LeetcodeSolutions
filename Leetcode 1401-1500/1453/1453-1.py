# Leetcode 1453: Maximum Number of Darts Inside of a Circular Dartboard
# https://leetcode.com/problems/maximum-number-of-darts-inside-of-a-circular-dartboard/
# Solved on 3rd of October, 2025
import math


class Solution:
    def numPoints(self, darts: list[list[int]], r: int) -> int:
        """
        Calculates the maximum number of darts that can be inside a circular dartboard of a given radius.

        Args:
            darts: A list of lists, where each inner list represents the [x, y] coordinates of a dart.
            r: The radius of the circular dartboard.
        Returns:
            The maximum number of darts that can be contained within a single circular dartboard of radius 'r'.
        """
        numDarts = len(darts)
        if numDarts <= 1:
            return numDarts

        maxPoints = 1

        for i in range(numDarts):
            for j in range(i + 1, numDarts):
                x1, y1 = darts[i]
                x2, y2 = darts[j]

                distSq = (x1 - x2) ** 2 + (y1 - y2) ** 2
                rSq = r * r

                if distSq > 4 * rSq:
                    continue

                dist = math.sqrt(distSq)

                midX = (x1 + x2) / 2
                midY = (y1 + y2) / 2

                h = math.sqrt(max(0, rSq - distSq / 4))

                dx = h * (y2 - y1) / dist
                dy = h * (x2 - x1) / dist

                c1x = midX + dx
                c1y = midY - dy

                c2x = midX - dx
                c2y = midY + dy

                centers = set([(c1x, c1y), (c2x, c2y)])
                epsilon = 1e-6

                for centerX, centerY in centers:
                    currentPoints = 0
                    for k in range(numDarts):
                        xK, yK = darts[k]

                        if (xK - centerX) ** 2 + (yK - centerY) ** 2 <= rSq + epsilon:
                            currentPoints += 1

                    maxPoints = max(maxPoints, currentPoints)

        return maxPoints