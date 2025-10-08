# Leetcode 2920: Maximum Points After Collecting Coins From All Nodes
# https://leetcode.com/problems/maximum-points-after-collecting-coins-from-all-nodes/
# Solved on 8th of October, 2025
class Solution:
    def maximumPoints(self, edges: list[list[int]], coins: list[int], k: int) -> int:
        """
        Calculates the maximum points achievable by collecting coins from nodes in a tree.

        Args:
            edges: A list of lists representing the connections between nodes.
            coins: A list of integers where coins[i] is the number of coins in node i.
            k: An integer representing the penalty for not halving coins at a node.

        Returns:
            The maximum points achievable.
        """

        numNodes = len(coins)
        adjList = [[] for _ in range(numNodes)]
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        memo = {}
        maxHalving = 16

        def dfs(node, parent, halving):
            if halving >= maxHalving:
                return 0

            state = (node, halving)
            if state in memo:
                return memo[state]

            currentCoins = coins[node] >> halving

            pointsWithPenality = currentCoins - k
            for neighbor in adjList[node]:
                if neighbor != parent:
                    pointsWithPenality += dfs(neighbor, node, halving)

            pointsWithHalving = currentCoins // 2
            for neighbor in adjList[node]:
                if neighbor != parent:
                    pointsWithHalving += dfs(neighbor, node, halving + 1)

            memo[state] = max(pointsWithPenality, pointsWithHalving)
            return memo[state]

        return dfs(0, -1, 0)