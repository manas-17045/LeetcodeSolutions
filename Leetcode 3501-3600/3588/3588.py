# Leetcode 3588: Find Maximum Area of a Triangle
# https://leetcode.com/problems/find-maximum-area-of-a-triangle/
# Solved on 25th of November, 2025
class Solution:
    def maxArea(self, coords: list[list[int]]) -> int:
        """
        Finds the maximum area of a triangle formed by any three points from the given coordinates.

        Args:
            coords: A list of lists, where each inner list represents a point [x, y].
        Returns:
            The maximum area of a triangle, or -1 if no triangle can be formed (less than 3 unique points).
        """
        minX = float('inf')
        maxX = float('-inf')
        minY = float('inf')
        maxY = float('-inf')
        xMap = {}
        yMap = {}

        for point in coords:
            x = point[0]
            y = point[1]

            if x < minX:
                minX = x
            if x > maxX:
                maxX = x
            if y < minY:
                minY = y
            if y > maxY:
                maxY = y

            if x not in xMap:
                xMap[x] = [y, y]
            else:
                if y < xMap[x][0]:
                    xMap[x][0] = y
                if y > xMap[x][1]:
                    xMap[x][1] = y

            if y not in yMap:
                yMap[y] = [x, x]
            else:
                if x < yMap[y][0]:
                    yMap[y][0] = x
                if x > yMap[y][1]:
                    yMap[y][1] = x

        result = 0

        for x in xMap:
            length = xMap[x][1] - xMap[x][0]
            if length > 0:
                area = length * max(x - minX, maxX - x)
                if area > result:
                    result = area

        for y in yMap:
            length = yMap[y][1] - yMap[y][0]
            if length > 0:
                area = length * max(y - minY, maxY - y)
                if area > result:
                    result = area

        if result == 0:
            return -1

        return result