# Leetcode 2603: Collect Coins in a Tree
# https://leetcode.com/problems/collect-coins-in-a-tree/
# Solved on 2nd of September, 2025
from collections import deque


class Solution:
    def collectTheCoins(self, coins: list[int], edges: list[list[int]]) -> int:
        """
        Calculates the minimum number of steps to collect all coins in a tree.

        Args:
            coins: A list of integers where coins[i] is 1 if the i-th node has a coin, and 0 otherwise.
            edges: A list of lists representing the connections between nodes in the tree.
        Returns:
            The minimum number of steps required to collect all coins.
        """
        n = len(coins)
        if n == 1:
            return 0

        # Build adjacency list and degree count
        g = [[] for _ in range(n)]
        deg = [0] * n
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
            deg[u] += 1
            deg[v] += 1

        # Remove leaves without coins
        q = deque([i for i in range(n) if deg[i] == 1 and coins[i] == 0])
        removed = [False] * n
        while q:
            u = q.popleft()
            removed[u] = True
            for v in g[u]:
                deg[v] -= 1
                if deg[v] == 1 and coins[v] == 0:
                    q.append(v)

        # Remove two layers of leaves (coins with distance <= 2)
        q = deque([i for i in range(n) if deg[i] == 1 and not removed[i]])
        for _ in range(2):
            for _ in range(len(q)):
                u = q.popleft()
                removed[u] = True
                for v in g[u]:
                    deg[v] -= 1
                    if deg[v] == 1 and not removed[v]:
                        q.append(v)

        # Count remaining edges
        remaining_edges = 0
        for u, v in edges:
            if not removed[u] or not removed[v]:
                remaining_edges += 1

        return max(0, remaining_edges * 2)