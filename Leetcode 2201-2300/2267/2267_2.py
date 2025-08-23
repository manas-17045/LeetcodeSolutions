# Leetcode 2267: Check if There Is a Valid Parentheses String Path
# https://leetcode.com/problems/check-if-there-is-a-valid-parentheses-string-path/
# Solved on 24th of August, 2025
class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        """
        Checks if there is a valid path from the top-left cell (0, 0) to the bottom-right cell (m-1, n-1)
        in a grid of parentheses, such that the path forms a balanced parentheses string.
        A path can only move right or down.

        Args:
            grid: A list of lists of strings, where each string is either '(' or ')'.
        Returns:
            True if a valid path exists, False otherwise.
        """
        m, n = len(grid), len(grid[0])
        # dp[i][j][balance] will store if we can reach (m-1, n-1) from (i,j) with this balance
        dp = [[{} for _ in range(n)] for __ in range(m)]

        def dfs(i: int, j: int, balance: int) -> bool:
            if balance < 0:
                return False

            if i == m - 1 and j == n - 1:
                # Final balance after including last cell
                return balance + (1 if grid[i][j] == '(' else -1) == 0

            if balance in dp[i][j]:
                return dp[i][j][balance]

            cur_balance = balance + (1 if grid[i][j] == '(' else -1)
            if cur_balance < 0:
                dp[i][j][balance] = False
                return False

            valid = False
            if i + 1 < m:
                valid = valid or dfs(i + 1, j, cur_balance)
            if j + 1 < n:
                valid = valid or dfs(i, j + 1, cur_balance)

            dp[i][j][balance] = valid
            return valid

        # Quick length check: minimum balance required is <= path length
        if (m + n - 1) % 2 != 0:
            return False

        return dfs(0, 0, 0)