# Leetcode 1515: Best Position for a Service Centre
# https://leetcode.com/problems/best-position-for-a-service-centre/
# Solved on 9th of September, 2025
import math


class Solution:
    def getMinDistSum(self, positions: list[list[int]]) -> float:
        """
        Calculates the minimum sum of Euclidean distances from a service center to all given positions.

        :param positions: A list of [x, y] coordinates representing the positions.
        :return: The minimum sum of distances.
        """
        def getDistSum(centerX: float, centerY: float) -> float:
            distSum = 0.0
            for posX, posY in positions:
                distX = posX - centerX
                distY = posY - centerY
                distSum += math.sqrt(distX * distX + distY * distY)
            return distSum

        numPositions = len(positions)
        if numPositions == 1:
            return 0.0

        currentX = sum(p[0] for p in positions) / numPositions
        currentY = sum(p[1] for p in positions) / numPositions

        step = 100.0
        epsilon = 1e-7

        minDistance = getDistSum(currentX, currentY)

        while step > epsilon:
            bestNextX = currentX
            bestNextY = currentY

            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

            for dx, dy in directions:
                nextX = currentX + dx * step
                nextY = currentY + dy * step

                nextDistance = getDistSum(nextX, nextY)

                if nextDistance < minDistance:
                    minDistance = nextDistance
                    bestNextX = nextX
                    bestNextY = nextY

            if bestNextX == currentX and bestNextY == currentY:
                step /= 2.0
            else:
                currentX = bestNextX
                currentY = bestNextY

        return minDistance