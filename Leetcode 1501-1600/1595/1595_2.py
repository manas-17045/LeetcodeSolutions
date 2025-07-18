# Leetcode 1595: Minimum Cost to Connect Two Groups of Points
# https://leetcode.com/problems/minimum-cost-to-connect-two-groups-of-points/
# Solved on 18th of July, 2025
class Solution:
    def connectTwoGroups(self, cost: list[list[int]]) -> int:
        """
        This function calculates the minimum cost to connect two groups of nodes.
        It uses dynamic programming to find the optimal connections.
        :param cost: A 2D list where cost[i][j] is the cost to connect node i from group 1 to node j from group 2.
        :return: The minimum total cost to connect all nodes in both groups.
        """
        m = len(cost)
        n = len(cost[0])
        if m < n:
            cost = [[cost[i][j] for i in range(m)] for j in range(n)]
            m, n = n, m
        maxMask = 1 << n
        INF = 10**18
        dp = [INF] * maxMask
        dp[0] = 0
        for i in range(m):
            ndp = [INF] * maxMask
            for mask in range(maxMask):
                base = dp[mask]
                if base == INF:
                    continue
                for j in range(n):
                    nm = mask | (1 << j)
                    c = base + cost[i][j]
                    if c < ndp[nm]:
                        ndp[nm] = c
            for mask in range(maxMask):
                for j in range(n):
                    nm = mask | (1 << j)
                    c = ndp[mask] + cost[i][j]
                    if c < ndp[nm]:
                        ndp[nm] = c
            dp = ndp
        return dp[maxMask - 1]