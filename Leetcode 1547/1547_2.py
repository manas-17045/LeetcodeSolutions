# Leetcode 1547: Minimum Cost to Cut a Stick
# https://leetcode.com/problems/minimum-cost-to-cut-a-stick/
# Solved on 16th of May, 2025

class Solution:
    def minCost(self, n: int, cuts: list[int]) -> int:
        """
        Calculates the minimum cost to cut a stick of length n at the given cut positions.

        Args:
            n: The length of the stick.
            cuts: A list of integers representing the positions where the stick should be cut.

        Returns:
            The minimum cost to cut the stick.
        """
        # Add the two stick endpoints and sort all cut positions
        pos = [0] + sorted(cuts) + [n]
        m = len(pos)

        # dp[i][j] = minimum cost to cut the segment (pos[i], pos[j])
        dp = [[0] * m for _ in range(m)]

        # Consider segments of increasing length (in terms of number of endpoints apart).
        # gap = j - i
        for gap in range(2, m):
            for i in range(0, m - gap):
                j = i + gap
                best = float('inf')
                cost = pos[j] - pos[i]
                # Try every possible first cut k between i and j
                for k in range(i + 1, j):
                    cur = dp[i][k] + dp[k][j] + cost
                    if cur < best:
                        best = cur
                dp[i][j] = best if best != float('inf') else 0

        # The answer for the full stick is dp[0][m - 1].
        return dp[0][m - 1]