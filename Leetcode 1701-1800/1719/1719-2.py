# Leetcode 1719: Number of Ways To Reconstruct a Tree
# https://leetcode.com/problems/number-of-ways-to-reconstruct-a-tree/
# Solved on 18th of September, 2025
from collections import defaultdict


class Solution:
    def checkWays(self, pairs: list[list[int]]) -> int:
        """
        Determines if a given set of pairs can form a valid tree structure and, if so, how many distinct ways.

        Args:
            pairs: A list of lists, where each inner list [a, b] represents an undirected edge between nodes a and b.
        Returns:
            An integer: 0 if no such tree exists, 1 if exactly one tree exists, or 2 if multiple trees exist.
        """
        # Build adjacency sets and collect nodes
        adj = defaultdict(set)
        nodes = set()
        for a, b in pairs:
            adj[a].add(b)
            adj[b].add(a)
            nodes.add(a)
            nodes.add(b)

        n = len(nodes)
        if n == 0:
            return 0

        # Find node with maximum degree (must be root: connected to all others)
        max_node = None
        max_deg = -1
        for u in nodes:
            d = len(adj[u])
            if d > max_deg:
                max_deg = d
                max_node = u

        # Root must be connected all other nodes
        if max_deg != n - 1:
            return 0

        root = max_node
        ways = 1

        # For every node except root, find a parent candidate among its neighbors.
        for u in nodes:
            if u == root:
                continue
            deg_u = len(adj[u])

            parent = None
            parent_deg = 10**9
            # Search among neighbors
            for v in adj[u]:
                dv = len(adj[v])
                if dv >= deg_u and dv < parent_deg:
                    parent = v
                    parent_deg = dv

            if parent is None:
                return 0

            # If parent's degree equals node's degree, the parent-child relation could be swapped -> ambiguous
            if parent_deg == deg_u:
                ways = 2

            # Validate: every neighbor of u must also be a neighbor of parent (except parent itself)
            for v in adj[u]:
                if v == parent:
                    continue
                if v not in adj[parent]:
                    return 0

        return ways