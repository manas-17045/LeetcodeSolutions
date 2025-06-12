# Leetcode 3288: Length of the Longest Increasing Path
# https://leetcode.com/problems/length-of-the-longest-increasing-path/
# Solved on 12th of June, 2025
from bisect import bisect_left


class FenwickMax:
    def __init__(self, n: int):
        self.n = n
        self.data = [0] * (n + 1)

    def update(self, i: int, val: int):
        while i <= self.n:
            if val > self.data[i]:
                self.data[i] = val
            i += i & -i

    def query(self, i: int) -> int:
        res = 0
        while i > 0:
            if self.data[i] > res:
                res = self.data[i]
            i -= i & -i
        return res

class Solution:
    def maxPathLength(self, coordinates: list[list[int]], k: int) -> int:
        """
        Finds the maximum length of a path starting and ending at coordinate k,
        where a path consists of a sequence of coordinates (x_1, y_1), (x_2, y_2), ..., (x_p, y_p)
        such that x_i < x_{i+1} and y_i < y_{i+1} for all i, or x_i > x_{i+1} and y_i > y_{i+1} for all i.

        Args:
            coordinates: A list of [x, y] coordinates.
            k: The index of the starting and ending coordinate.
        Returns: The maximum path length.
        """
        n = len(coordinates)
        # Compress y
        ys = sorted({y for _, y in coordinates})
        m = len(ys)
        y_comp = [bisect_left(ys, y) + 1 for _, y in coordinates]

        # Build list of (x, y_comp, index)
        pts = [(coordinates[i][0], y_comp[i], i) for i in range(n)]

        # Forward pass: compute dp1[i] = LIS length ending at i
        dp1 = [0] * n
        BIT = FenwickMax(m)
        # Sort by x increasing
        pts.sort(key=lambda t: t[0])
        # Process in groups of equal x so that we don't chain within same-x
        i = 0
        while i < n:
            j = i
            # Find range [i...j) with same x
            while j < n and pts[j][0] == pts[i][0]:
                j += 1
            # For each in group, query BIT
            for x, yc, idx in pts[i:j]:
                dp1[idx] = BIT.query(yc - 1) + 1
            # Update BIT
            for x, yc, idx in pts[i:j]:
                BIT.update(yc, dp1[idx])
            i = j

        # Backward pass
        dp2 = [0] * n
        BIT = FenwickMax(m)
        pts_rev = [(x, (m + 1) - yc, idx) for x, yc, idx in pts]
        # Sort by x descending
        pts_rev.sort(key= lambda t: -t[0])
        i = 0
        while i < n:
            j = i
            while j < n and pts_rev[j][0] == pts_rev[i][0]:
                j += 1
            for x, yRev, idx in pts_rev[i:j]:
                dp2[idx] = BIT.query(yRev - 1) + 1
            for x, yRev, idx in pts_rev[i:j]:
                BIT.update(yRev, dp2[idx])
            i = j

        # Answer for point k
        return dp1[k] + dp2[k] - 1