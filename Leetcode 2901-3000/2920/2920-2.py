# Leetcode 2920: Maximum Points After Collecting Coins From All Nodes
# https://leetcode.com/problems/maximum-points-after-collecting-coins-from-all-nodes/
# Solved on 8th of October, 2025
from collections import defaultdict


class Solution:
    def maximumPoints(self, edges: list[list[int]], coins: list[int], k: int) -> int:
        """
        Calculates the maximum points obtainable by traversing a tree,
        where at each node, you can either collect `coins[node] - k` points
        or `coins[node] / 2` points, affecting subsequent coin values.
        :param edges: A list of lists representing the edges of the tree.
        :param coins: A list of integers where coins[i] is the number of coins at node i.
        :param k: An integer representing the cost to collect coins in the first strategy.
        :return: The maximum points that can be obtained.
        """
        n = len(coins)

        # Build adjacency list
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        # Memoization: (node, halvings) -> max points
        memo = {}

        def dfs(node: int, parent: int, halvings: int) -> int:
            # If we've halved too many times, coins become 0
            if halvings >= 20:  # 10^4 >> 20 times gives 0
                halvings = 20

            if (node, halvings) in memo:
                return memo[(node, halvings)]

            # Current coins at this node after halvings
            current_coins = coins[node] >> halvings

            # Strategy 1: Collect all coins, get (current_coins - k) points
            # Then recursively collect from children with same halving count
            points1 = current_coins - k
            for child in graph[node]:
                if child != parent:
                    points1 += dfs(child, node, halvings)

            # Strategy 2: Collect all coins, get floor(current_coins / 2) points
            # Then recursively collect from children with halvings + 1
            points2 = current_coins >> 1
            for child in graph[node]:
                if child != parent:
                    points2 += dfs(child, node, halvings + 1)

            result = max(points1, points2)
            memo[(node, halvings)] = result
            return result

        # Start DFS from root node 0 with 0 halvings
        return dfs(0, -1, 0)