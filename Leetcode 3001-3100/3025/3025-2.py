# Leetcode 3025: Find the Number of Ways to Place People I
# https://leetcode.com/problems/find-the-number-of-ways-to-place-people-i/
# Solved on 2nd of September. 2025
class Solution:
    def numberOfPairs(self, points: list[list[int]]) -> int:
        """
        Calculates the number of "beautiful" pairs of points.
        A pair of points (p_i, p_j) is beautiful if p_i[0] <= p_j[0], p_j[1] <= p_i[1],
        and there is no other point p_k such that p_i[0] <= p_k[0] <= p_j[0] and p_j[1] <= p_k[1] <= p_i[1].

        Args:
            points: A list of points, where each point is [x, y].
        Returns:
            The total number of beautiful pairs.
        """
        # Sort by x ascending, then by y descending (to ease comparisons)
        points.sort(key=lambda p: (p[0], -p[1]))
        n = len(points)
        ans = 0

        # For each pair (i, j) with i < j
        for i in range(n):
            for j in range(i + 1, n):
                if points[i][1] < points[j][1]:
                    continue

                valid = True
                # Check no point strictly, inside rectangle
                for k in range(i + 1, j):
                    if points[i][0] <= points[k][0] <= points[j][0] and points[j][1] <= points[k][1] <= points[i][1]:
                        valid = False
                        break

                if valid:
                    ans += 1

        return ans