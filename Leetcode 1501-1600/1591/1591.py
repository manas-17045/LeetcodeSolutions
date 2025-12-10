# Leetcode 1591: Strange Printer II
# https://leetcode.com/problems/strange-printer-ii/
# Solved on 10th of December, 2025
class Solution:
    def isPrintable(self, targetGrid: list[list[int]]) -> bool:
        """
        Determines if the targetGrid can be formed by printing colored rectangles.

        Args:
            targetGrid (list[list[int]]): A 2D list representing the final grid.
        Returns:
            bool: True if the grid can be formed, False otherwise.
        """
        rows = len(targetGrid)
        cols = len(targetGrid[0])
        colorBounds = {}
        uniqueColors = set()

        for r in range(rows):
            for c in range(cols):
                color = targetGrid[r][c]
                uniqueColors.add(color)
                if color not in colorBounds:
                    colorBounds[color] = [r, r, c, c]
                else:
                    bounds = colorBounds[color]
                    bounds[0] = min(bounds[0], r)
                    bounds[1] = max(bounds[1], r)
                    bounds[2] = min(bounds[2], c)
                    bounds[3] = max(bounds[3], c)

        dependencyGraph = {c: set() for c in uniqueColors}

        for color in uniqueColors:
            minR, maxR, minC, maxC = colorBounds[color]
            for r in range(minR, maxR + 1):
                for c in range(minC, maxC + 1):
                    pixelColor = targetGrid[r][c]
                    if pixelColor != color:
                        dependencyGraph[color].add(pixelColor)

        visitedStatus = {}

        def hasCycle(node):
            state = visitedStatus.get(node, 0)
            if state == 1:
                return True
            if state == 2:
                return False

            visitedStatus[node] = 1
            for neighbor in dependencyGraph[node]:
                if hasCycle(neighbor):
                    return True

            visitedStatus[node] = 2
            return False

        for color in uniqueColors:
            if hasCycle(color):
                return False

        return True