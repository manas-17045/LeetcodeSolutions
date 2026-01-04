# Leetcode 3047: Find the Largest Area of Square Inside Two Rectangles
# https://leetcode.com/problems/find-the-largest-area-of-square-inside-two-rectangles/
# Solved on 4th of January, 2026
class Solution:
    def largestSquareArea(self, bottomLeft: list[list[int]], topRight: list[list[int]]) -> int:
        """
        Finds the largest area of a square that can be formed by the intersection of any two rectangles.

        Args:
            bottomLeft: A list of [x, y] coordinates for the bottom-left corner of each rectangle.
            topRight: A list of [x, y] coordinates for the top-right corner of each rectangle.
        Returns:
            The largest possible area of a square that can be formed within the intersection of any two rectangles.
        """
        maxSide = 0
        n = len(bottomLeft)

        for i in range(n):
            for j in range(i + 1, n):
                minX = max(bottomLeft[i][0], bottomLeft[j][0])
                maxX = min(topRight[i][0], topRight[j][0])
                minY = max(bottomLeft[i][1], bottomLeft[j][1])
                maxY = min(topRight[i][1], topRight[j][1])

                if minX < maxX and minY < maxY:
                    side = min(maxX - minX, maxY - minY)
                    if side > maxSide:
                        maxSide = side

        return maxSide * maxSide