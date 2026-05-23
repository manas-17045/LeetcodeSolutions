# Leetcode 3923: Minimum Generations to Target Point
# https://leetcode.com/problems/minimum-points-to-target-point/
# Solved on 23rd of May, 2026
class Solution:
    def minGenerations(self, points: list[list[int]], target: list[int]) -> int:
        """
        Calculates the minimum number of generations required to reach a target point
        by iteratively generating midpoints from existing points.

        :param points: A list of initial 3D coordinates.
        :param target: The target 3D coordinate to reach.
        :return: The minimum number of generations to reach the target, or -1 if impossible.
        """
        targetTuple = tuple(target)
        seenPoints = set()
        activePoints = []
        for currentPoint in points:
            pointTuple = tuple(currentPoint)
            if pointTuple not in seenPoints:
                seenPoints.add(pointTuple)
                activePoints.append(pointTuple)

        if targetTuple in seenPoints:
            return 0

        genCount = 0
        startIndex = 0
        endIndex = len(activePoints)
        while startIndex < endIndex:
            genCount += 1
            nextGenPoints = set()
            for i in range(endIndex):
                innerStart = max(i + 1, startIndex)
                for j in range(innerStart, endIndex):
                    pOne = activePoints[i]
                    pTwo = activePoints[j]
                    midPoint = ((pOne[0] + pTwo[0]) // 2, (pOne[1] + pTwo[1]) // 2, (pOne[2] + pTwo[2]) // 2)
                    if midPoint not in seenPoints:
                        nextGenPoints.add(midPoint)

            if targetTuple in nextGenPoints:
                return genCount

            if not nextGenPoints:
                return -1

            startIndex = endIndex
            for newPoint in nextGenPoints:
                activePoints.append(newPoint)
                seenPoints.add(newPoint)

            endIndex = len(activePoints)

        return -1