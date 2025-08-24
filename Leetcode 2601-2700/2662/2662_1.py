# Leetcode 2662: Minimum Cost of a Path With Special Roads
# https://leetcode.com/problems/minimum-cost-of-a-path-with-special-roads/
# Solved on 24th of August, 2025
import heapq


class Solution:
    def minimumCost(self, start: list[int], target: list[int], specialRoads: list[list[int]]) -> int:
        """
        Calculates the minimum cost to travel from a start point to a target point,
        considering both direct travel and special roads.
        :param start: A list representing the starting coordinates [startX, startY].
        :param target: A list representing the target coordinates [targetX, targetY].
        :param specialRoads: A list of special roads, where each road is [x1, y1, x2, y2, cost].
        :return: The minimum cost to reach the target.
        """
        targetX = target[0]
        targetY = target[1]
        startX = start[0]
        startY = start[1]

        startPoint = (startX, startY)

        dist = {}

        pq = [(0, startPoint)]

        minCost = abs(startX - targetX) + abs(startY - targetY)

        while pq:
            currentCost, currentPoint = heapq.heappop(pq)
            cx, cy = currentPoint

            if currentCost > dist.get(currentPoint, float('inf')):
                continue

            minCost = min(minCost, currentCost + abs(cx - targetX) + abs(cy - targetY))

            for x1, y1, x2, y2, roadCost in specialRoads:
                destPoint = (x2, y2)

                travelToRoadCost = abs(cx - x1) + abs(cy - y1)

                newCostToDest = currentCost + travelToRoadCost + roadCost

                if newCostToDest < dist.get(destPoint, float('inf')):
                    dist[destPoint] = newCostToDest
                    heapq.heappush(pq, (newCostToDest, destPoint))

        return minCost