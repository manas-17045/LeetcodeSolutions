# Leetcode 2872: Maximum Number of K-Divisible Components
# https://leetcode.com/problems/maximum-number-of-k-divisible-components/
# Solved on 13th of June, 2025

class Solution:
    def maxKDivisibleComponents(self, n: int, edges: list[list[int]], values: list[int], k: int) -> int:
        """
        Given a tree with n nodes, where each node has a value, and an integer k,
        find the maximum number of connected components you can obtain by removing
        some edges such that the sum of values in each component is divisible by k.

        Args:
            n: The number of nodes in the tree.
            edges: A list of edges representing the tree.
            values: A list of values for each node.
            k: The divisor.
        """
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        self.count = 0

        def dfs(node, parent):
            currentSum = values[node]
            for neighbor in adj[node]:
                if neighbor != parent:
                    currentSum += dfs(neighbor, node)

            if currentSum % k == 0:
                self.count += 1
                return 0

            return currentSum

        dfs(0, -1)
        return self.count