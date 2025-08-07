# Leetcode 3363: Find the Maximum Number of Fruits Collected
# https://leetcode.com/problems/find-the-maximum-number-of-fruits-collected/
# Solved on 7th of August, 2025
class Solution:
    def maxCollectedFruits(self, fruits: list[list[int]]) -> int:
        """
        Calculates the maximum number of fruits that can be collected based on three different paths: top-left diagonal, top-right path, and bottom-left path.

        Args:
            fruits: A list of lists of integers representing the fruits available at each position.

        Returns:
            An integer representing the total maximum fruits collected.
        """
        n = len(fruits)

        def getTopLeft() -> int:
            return sum(fruits[i][i] for i in range(n))

        def getTopRight() -> int:
            dp = [[0] * n for _ in range(n)]
            dp[0][n-1] = fruits[0][n-1]
            for x in range(n):
                for y in range(n):
                    if x >= y and (x, y) != (n-1, n-1):
                        continue
                    for dx, dy in [(1, -1), (1, 0), (1, 1)]:
                        i, j = x - dx, y - dy
                        if not (0 <= i < n and 0 <= j < n):
                            continue
                        if i < j < n-1 - i:
                            continue
                        dp[x][y] = max(dp[x][y], dp[i][j] + fruits[x][y])
            return dp[n-1][n-1]

        def getBottomLeft() -> int:
            dp = [[0] * n for _ in range(n)]
            dp[n-1][0] = fruits[n-1][0]
            for y in range(n):
                for x in range(n):
                    if x <= y and (x, y) != (n-1, n-1):
                        continue
                    for dx, dy in [(-1, 1), (0, 1), (1, 1)]:
                        i, j = x - dx, y - dy
                        if not (0 <= i < n and 0 <= j < n):
                            continue
                        if j < i < n-1 - j:
                            continue
                        dp[x][y] = max(dp[x][y], dp[i][j] + fruits[x][y])
            return dp[n-1][n-1]

        return getTopLeft() + getTopRight() + getBottomLeft() - 2 * fruits[-1][-1]