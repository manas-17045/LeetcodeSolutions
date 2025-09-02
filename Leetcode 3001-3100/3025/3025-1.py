# Leetcode 3025: Find the Number of Ways to Place People I
# https://leetcode.com/problems/find-the-number-of-ways-to-place-people-i/
# Solved on 2nd of September. 2025
class Solution:
    def numberOfPairs(self, points: list[list[int]]) -> int:
        """
        Finds the number of ways to place two people such that the first person is at point A,
        the second person is at point B, and point B is to the right and below or at the same y-level as point A,
        and there are no other points within the rectangle formed by A and B.

        Args:
            points: A list of points, where each point is represented as [x, y].
        Returns:
            The total number of valid pairs (A, B).
        """
        points.sort(key=lambda p: (p[0], -p[1]))

        numPoints = len(points)
        count = 0

        for i in range(numPoints):
            yI = points[i][1]
            maxYForThisI = -1

            for j in range(i + 1, numPoints):
                yJ = points[j][1]

                if yJ <= yI:
                    if maxYForThisI < yJ:
                        count += 1
                    maxYForThisI = max(maxYForThisI, yJ)

        return count