# Leetcode 3380: Maximum Area Rectangle With Point Constraints I
# https://leetcode.com/problems/maximum-area-rectangle-with-point-constraints-i/
# Solved on 1st of January, 2025
class Solution:
    def maxRectangleArea(self, points: list[list[int]]) -> int:
        """
        Calculates the maximum area of a rectangle formed by four points from the given set of points,
        such that all four corner points of the rectangle are present in the input `points`.

        :param points: A list of lists, where each inner list `[x, y]` represents a point.
        :return: The maximum area of such a rectangle. Returns -1 if no such rectangle can be formed.
        """
        pointSet = set()
        for point in points:
            pointSet.add((point[0], point[1]))

        maxArea = -1
        numPoints = len(points)

        for i in range(numPoints):
            for j in range(i + 1, numPoints):
                x1 = points[i][0]
                y1 = points[i][1]
                x2 = points[j][0]
                y2 = points[j][1]

                if x1 == x2 or y1 == y2:
                    continue

                if (x1, y2) in pointSet and (x2, y1) in pointSet:
                    minX = min(x1, x2)
                    maxX = max(x1, x2)
                    minY = min(y1, y2)
                    maxY = max(y1, y2)

                    pointsInRect = 0
                    for k in range(numPoints):
                        px = points[k][0]
                        py = points[k][1]

                        if px >= minX and px <= maxX and py >= minY and py <= maxY:
                            pointsInRect += 1

                    if pointsInRect == 4:
                        currentArea = (maxX - minX) * (maxY - minY)
                        if currentArea > maxArea:
                            maxArea = currentArea

        return maxArea