# Leetcode 1478: Allocate Mailboxes
# https://leetcode.com/problems/allocate-mailboxes/
# Solved on 19th of July, 2025
class Solution:
    def minDistance(self, houses: list[int], k: int) -> int:
        """
        Calculates the minimum total distance between houses and k mailboxes.

        Args:
            houses (list[int]): A list of integers representing the positions of houses.
            k (int): The number of mailboxes to be placed.

        Returns:
            int: The minimum total distance.
        """
        n = len(houses)
        houses.sort()

        cost = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                m = (i + j) // 2

                s = 0
                for t in range(i, (j + 1)):
                    s += abs(houses[t] - houses[m])
                cost[i][j] = s

        INF = 10**18
        dp = [[INF] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        # Fill dp
        for i in range(1, (n + 1)):
            for t in range(1, (k + 1)):
                # Try placing the t-th mailbox to cover houses
                for p in range(i):
                    dp[i][t] = min(dp[i][t], dp[p][t - 1] + cost[p][i - 1])

        return dp[n][k]