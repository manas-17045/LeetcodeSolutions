# Leetcode 3772: Maximum Subgraph Score in a Tree
# https://leetcode.com/problems/maximum-subgraph-score-in-a-tree/
# Solved on 23rd of December, 2025
class Solution:
    def maxSubgraphScore(self, n: int, edges: list[list[int]], good: list[int]) -> list[int]:
        """
        Calculates the maximum subgraph score for each node in a tree.

        Args:
            n: The number of nodes in the tree.
            edges: A list of lists representing the edges of the tree.
            good: A list of integers where good[i] is 1 if node i is good, and 0 otherwise.

        Returns:
            A list of integers, where the i-th element is the maximum subgraph score for node i.
        """
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        weights = [1 if g == 1 else -1 for g in good]

        order = [0]
        visited = [False] * n
        visited[0] = True
        parents = [-1] * n

        head = 0
        while head < len(order):
            u = order[head]
            head += 1
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    parents[v] = u
                    order.append(v)

        dp = list(weights)

        for i in range(n - 1, -1, -1):
            u = order[i]
            p = parents[u]
            if p != -1:
                if dp[u] > 0:
                    dp[p] += dp[u]

        ans = [0] * n
        ans[0] = dp[0]

        for i in range(1, n):
            u = order[i]
            p = parents[u]

            scoreFromParent = ans[p]
            if dp[u] > 0:
                scoreFromParent -= dp[u]

            ans[u] = dp[u]
            if scoreFromParent > 0:
                ans[u] += scoreFromParent

        return ans