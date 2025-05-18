# Leetcode 1931: Painting a Grid With Three Different Colors
# https://leetcode.com/problems/painting-a-grid-with-three-different-colors/
# Solved on 18th of May, 2025

class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        """
        Calculates the number of ways to color an m x n grid with three colors such that no two adjacent cells have
        the same color.

        Args:
            m: The number of rows in the grid.
            n: The number of columns in the grid.

        Returns:
            The number of valid colorings modulo 10^9 + 7.
        """
        MOD = 10**9 + 7

        # Generate all valid single-column colorings (no two vertical neighbors equal)
        patterns = []
        def dfs(pos: int, col: list[int]):
            if pos == m:
                patterns.append(tuple(col))
                return
            for color in range(3):
                if pos > 0 and col[pos - 1] == color:
                    continue
                col.append(color)
                dfs(pos + 1, col)
                col.pop()

        dfs(0, [])
        P = len(patterns)

        # Precompute compatibility: Two columns must differ at every row (no horizontal same)
        compat = [[] for _ in range(P)]
        for i in range(P):
            pi = patterns[i]
            for j in range(P):
                pj = patterns[j]
                # Check no row has the same color in both columns
                for row in range(m):
                    if pi[row] == pj[row]:
                        break
                    else:
                        compat[i].append(j)

        # dp[c] = number of ways ending with pattern c in the current column
        dp = [1] * P

        # For each further column, transition via compatibilities
        for _ in range(n - 1):
            new_dp = [0] * P
            for prev in range(P):
                cnt = dp[prev]
                if cnt:
                    for nxt in compat[prev]:
                        new_dp[nxt] = (new_dp[nxt] + cnt) % MOD
            dp = new_dp

        # Total ways is sum over patterns in the last column
        return sum(dp) % MOD