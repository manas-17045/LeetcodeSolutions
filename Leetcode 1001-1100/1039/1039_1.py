# Leetcode 1039: Minimum Score Triangulation of Polygon
# https://leetcode.com/problems/minimum-score-triangulation-of-polygon/
# Solved on 4th of August, 2025
class Solution:
    def minScoreTriangulation(self, values: list[int]) -> int:
        """
        Calculates the minimum score triangulation of a convex `n`-sided polygon.

        Args:
            values (list[int]): A list of integers representing the values of the vertices of the polygon in clockwise order.
        Returns:
            int: The minimum score of the triangulation.
        """
        numVertices = len(values)
        dpTable = [[0] * numVertices for _ in range(numVertices)]

        for length in range(3, (numVertices + 1)):
            for i in range(numVertices - length + 1):
                j = i + length - 1
                dpTable[i][j] = float('inf')
                for k in range(i + 1, j):
                    currentScore = dpTable[i][k] + dpTable[k][j] + values[i] * values[k] * values[j]
                    if currentScore < dpTable[i][j]:
                        dpTable[i][j] = currentScore

        return dpTable[0][numVertices - 1]