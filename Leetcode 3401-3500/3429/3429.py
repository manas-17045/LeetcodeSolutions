# Leetcode 3429: Paint House IV
# https://leetcode.com/problems/paint-house-iv/
# Solved on 23rd of November, 2025
class Solution:
    def minCost(self, n: int, cost: list[list[int]]) -> int:
        """
        Calculates the minimum cost to paint n houses such that no two adjacent houses have the same color.
        This problem is a variation where houses are painted in pairs from the ends towards the center.

        Args:
            n (int): The total number of houses.
            cost (list[list[int]]): A 2D list where cost[i][j] is the cost to paint house i with color j.

        Returns:
            int: The minimum cost to paint all houses.
        """
        limit = n // 2
        dp = [[float('inf')] * 3 for _ in range(3)]

        for i in range(3):
            for j in range(3):
                if i != j:
                    dp[i][j] = cost[0][i] + cost[n - 1][j]

        for i in range(1, limit):
            newDp = [[float('inf')] * 3 for _ in range(3)]

            for curLeft in range(3):
                for curRight in range(3):
                    if curLeft == curRight:
                        continue

                    currentCost = cost[i][curLeft] + cost[n - 1 - i][curRight]
                    minPrev = float('inf')

                    for prevLeft in range(3):
                        if prevLeft == curLeft:
                            continue
                        for prevRight in range(3):
                            if prevRight == curRight:
                                continue

                            if dp[prevLeft][prevRight] < minPrev:
                                minPrev = dp[prevLeft][prevRight]

                    if minPrev != float('inf'):
                        newDp[curLeft][curRight] = minPrev + currentCost

            dp = newDp

        ans = float('inf')
        for i in range(3):
            for j in range(3):
                if dp[i][j] < ans:
                    ans = dp[i][j]

        return int(ans)