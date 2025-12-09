# Leetcode 3225: Maximum Score From Grid Operations
# https://leetcode.com/problems/maximum-score-from-grid-operations/
# Solved on 9th of December, 2025
class Solution:
    def maximumScore(self, grid: list[list[int]]) -> int:
        """
        Calculates the maximum score achievable from grid operations.

        Args:
            grid: A list of lists of integers representing the grid.
        Returns:
            An integer representing the maximum score.
        """
        n = len(grid)

        col_prefix = [[0] * (n + 1) for _ in range(n)]
        for j in range(n):
            for i in range(n):
                col_prefix[j][i + 1] = col_prefix[j][i] + grid[i][j]

        def get_score(c, l, r):
            if l >= r:
                return 0
            return col_prefix[c][r] - col_prefix[c][l]

        dp = [[-1] * (n + 1) for _ in range(n + 1)]

        for h in range(n + 1):
            dp[0][h] = 0

        for j in range(n):
            new_dp = [[-1] * (n + 1) for _ in range(n + 1)]

            for curr in range(n + 1):
                col_vals = [row[curr] for row in dp]

                pre_max_d = [-1] * (n + 1)
                running_max = -1
                for k in range(n + 1):
                    if col_vals[k] > running_max:
                        running_max = col_vals[k]
                    pre_max_d[k] = running_max

                suf_max_t = [-1] * (n + 2)
                running_max = -1
                for k in range(n, -1, -1):
                    val = col_vals[k]
                    if val != -1:
                        s = val + get_score(j, curr, k)
                        if s > running_max:
                            running_max = s
                    suf_max_t[k] = running_max

                for next_h in range(n + 1):
                    m1 = -1
                    if pre_max_d[next_h] != -1:
                        m1 = pre_max_d[next_h] + get_score(j, curr, next_h)

                    m2 = suf_max_t[next_h + 1]

                    new_dp[curr][next_h] = max(m1, m2)

            dp = new_dp

        ans = 0
        for curr in range(n + 1):
            ans = max(ans, dp[curr][0])

        return ans