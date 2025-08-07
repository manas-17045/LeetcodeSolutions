# Leetcode 3363: Find the Maximum Number of Fruits Collected
# https://leetcode.com/problems/find-the-maximum-number-of-fruits-collected/
# Solved on 7th of August, 2025
class Solution:
    def maxCollectedFruits(self, fruits: list[list[int]]) -> int:
        """
        Calculates the maximum number of fruits that can be collected from a grid.

        Args:
            fruits: A 2D list of integers representing the number of fruits in each cell of the grid.

        Returns:
            The maximum number of fruits that can be collected.
        """
        return self.getTopLeft(fruits) + self.getTopRight(fruits) + self.getBottomLeft(fruits) - 2 * fruits[-1][-1]
    
    def getTopLeft(self, fruits: list[list[int]]) -> int:
        n = len(fruits)
        res = 0
        for i in range(n):
            res += fruits[i][i]
        return res
    
    def getTopRight(self, fruits: list[list[int]]) -> int:
        n = len(fruits)
        dp = [[0] * n for _ in range(n)]
        dp[0][n - 1] = fruits[0][n - 1]
        for x in range(n):
            for y in range(n):
                if x >= y and not (x == n - 1 and y == n - 1):
                    continue
                for dx, dy in [(1, -1), (1, 0), (1, 1)]:
                    i = x - dx
                    j = y - dy
                    if not (0 <= i < n and 0 <= j < n):
                        continue
                    if i < j and j < (n - 1 - i):
                        continue
                    dp[x][y] = max(dp[x][y], dp[i][j] + fruits[x][y])
        return dp[n - 1][n - 1]
    
    def getBottomLeft(self, fruits: list[list[int]]) -> int:
        n = len(fruits)
        dp = [[0] * n for _ in range(n)]
        dp[n - 1][0] = fruits[n - 1][0]
        for y in range(n):
            for x in range(n):
                if x <= y and not (x == n - 1 and y == n - 1):
                    continue
                for dx, dy in [(-1, -1), (0, 1), (1, 1)]:
                    i = x - dx
                    j = y - dy
                    if not (0 <= i < n and 0 <= j < n):
                        continue
                    if j < i and i < n - 1 - j:
                        continue
                    dp[x][y] = max(dp[x][y], dp[i][j] + fruits[x][y])
        return dp[n - 1][n - 1]