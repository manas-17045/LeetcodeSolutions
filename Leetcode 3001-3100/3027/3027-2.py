# Leetcode 3027: Find the Number of Ways to Place People II
# https://leetcode.com/problems/find-the-number-of-ways-to-place-people-ii/
# Solved on 3rd of September, 2025
class Solution:
    def numberOfPairs(self, points: list[list[int]]) -> int:
        """
        Calculates the number of "beautiful" pairs of points.
        A pair of points (p1, p2) is beautiful if p1.x <= p2.x, p1.y >= p2.y,
        and there is no other point p3 such that p1.x <= p3.x <= p2.x and p2.y <= p3.y <= p1.y.

        Args:
            points: A list of points, where each point is [x, y].
        Returns:
            The total number of beautiful pairs.
        """
        # Sort by x ascending, then y descending to get a stable left-to-right scan.
        points.sort(key=lambda p: (p[0], -p[1]))
        n = len(points)
        ans = 0

        for i in range(n):
            ay = points[i][1]
            # Track the maximum y among points in (i, j) that are <= ay
            max_y_between = -10**19
            for j in range(i + 1, n):
                by = points[j][1]
                if by <= ay:
                    # Valid iff no in-between y lies in [by, ay]
                    if max_y_between < by:
                        ans += 1
                    # Incorporate this point for subsequent checks
                    if by > max_y_between:
                        max_y_between = by

        return ans