# Leetcode 3288: Length of the Longest Increasing Path
# https://leetcode.com/problems/length-of-the-longest-increasing-path/
# Solved on 12th of June, 2025

class FenwickTree:
    def __init__(self, size):
        self.tree = [0] * (size + 1)

    def update(self, i, val):
        while i < len(self.tree):
            self.tree[i] = max(self.tree[i], val)
            i += i & -i

    def query(self, i):
        maxVal = 0
        while i > 0:
            maxVal = max(self.tree[i], maxVal)
            i -= i & -i
        return maxVal

class Solution:
    def maxPathLength(self, coordinates: list[list[int]], k: int) -> int:
        """
        Calculates the length of the longest path that passes through the k-th point
        in a set of 2D coordinates, where a path is defined by points with strictly
        increasing x and y coordinates.
        :param coordinates: A list of [x, y] coordinates.
        :param k: The index of the point that must be included in the path (0-indexed).
        """
        n = len(coordinates)
        if n == 0:
            return 0

        pointsFwd = [(coordinates[i][0], coordinates[i][1], i) for i in range(n)]
        dpEnding = self.calculateDP(pointsFwd, n)

        pointsBwd = [(-coordinates[i][0], -coordinates[i][1], i) for i in range(n)]
        dpStarting = self.calculateDP(pointsBwd, n)

        return dpEnding[k] + dpStarting[k] - 1

    def calculateDP(self, points, n):
        points.sort()

        allY = sorted(list(set(p[1] for p in points)))
        yMap = {y: i + 1 for i, y in enumerate(allY)}

        bit = FenwickTree(len(yMap))
        dp = [0] * n
        i = 0
        while i < n:
            j = i
            while j < n and points[j][0] == points[i][0]:
                j += 1

            groupResults = []
            for l in range(i, j):
                px, py, originalIdx = points[l]
                compressedY = yMap[py]
                maxPrevDp = bit.query(compressedY - 1)
                currentDp = 1 + maxPrevDp
                groupResults.append((compressedY, currentDp, originalIdx))

            for compressedY, currentDp, originalIdx in groupResults:
                bit.update(compressedY, currentDp)
                dp[originalIdx] = currentDp

            i = j

        return max(dp)