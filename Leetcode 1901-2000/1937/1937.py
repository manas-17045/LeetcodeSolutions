# Leetcode 1937: Maximum Number of Points with Cost
# https://leetcode.com/problems/maximum-number-of-points-with-cost/
# Solved on 30th of November, 2025
class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        """
        Calculates the maximum number of points that can be obtained by selecting one cell from each row,
        with a cost penalty for selecting cells further apart in adjacent rows.

        :param points: A list of lists of integers representing the points in each cell.
        :return: The maximum number of points achievable.
        """
        rows = len(points)
        cols = len(points[0])
        prevRow = points[0]

        for r in range(1, rows):
            currRow = [0] * cols
            runningMax = float('-inf')

            for c in range(cols):
                runningMax = max(runningMax - 1, prevRow[c])
                currRow[c] = runningMax

            runningMax = float('-inf')
            for c in range(cols - 1, -1, -1):
                runningMax = max(runningMax - 1, prevRow[c])
                currRow[c] = max(currRow[c], runningMax) + points[r][c]

            prevRow = currRow

        return max(prevRow)