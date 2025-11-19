# Leetcode 3102: Minimize Manhattan Distances
# https://leetcode.com/problems/minimize-manhattan-distances/
# Solved on 19th of November, 2025
class Solution:
    def minimizeManhattanDistance(self, points: list[list[int]]) -> int:
        """
        Minimizes the maximum Manhattan distance between any two points after removing one point.

        Args:
            points: A list of lists, where each inner list `[x, y]` represents a point.
        Returns:
            The minimum possible maximum Manhattan distance after removing one point.
        """
        sums = []
        diffs = []
        for i, point in enumerate(points):
            sums.append((point[0] + point[1], i))
            diffs.append((point[0] - point[1], i))

        sums.sort()
        diffs.sort()

        candidates = {sums[0][1], sums[-1][1], diffs[0][1], diffs[-1][1]}
        minMaxDist = float('inf')

        for index in candidates:
            if sums[0][1] == index:
                minSum = sums[1][0]
            else:
                minSum = sums[0][0]

            if sums[-1][1] == index:
                maxSum = sums[-2][0]
            else:
                maxSum = sums[-1][0]

            if diffs[0][1] == index:
                minDiff = diffs[1][0]
            else:
                minDiff = diffs[0][0]

            if diffs[-1][1] == index:
                maxDiff = diffs[-2][0]
            else:
                maxDiff = diffs[-1][0]

            currentMaxDist = max(maxSum - minSum, maxDiff - minDiff)
            minMaxDist = min(minMaxDist, currentMaxDist)

        return minMaxDist