# Leetcode 1039: Minimum Score Triangulation of Polygon
# https://leetcode.com/problems/minimum-score-triangulation-of-polygon/
# Solved on 4th of August, 2025
class Solution:
    def minScoreTriangulation(self, values: list[int]) -> int:
        """
        Calculates the minimum score to triangulate a convex polygon.
        :param values: A list of integers representing the values of the vertices of the polygon.
        :return: The minimum score to triangulate the polygon.
        """
        n = len(values)
        # dp[i][j] = minimum score to triangulate the sub-polygon from i to j (inclusive)
        dp = [[0] * n for _ in range(n)]

        # Consider all sub-polygons of length L = 3,4,...,n
        for L in range(3, n + 1):
            for i in range(n - L + 1):
                j = i + L - 1
                best = float('inf')
                # Try all ways to pick the last triangle (i, k, j)
                for k in range(i + 1, j):
                    cost = dp[i][k] + dp[k][j] + values[i] * values[k] * values[j]
                    if cost < best:
                        best = cost
                dp[i][j] = best

        return dp[0][n - 1]