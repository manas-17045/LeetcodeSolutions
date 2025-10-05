# Leetcode 3559: Number of Ways to Assign Edge Weights II
# https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-ii/
# Solved on 5th of October, 2025
from collections import defaultdict, deque


class Solution:
    def assignEdgeWeights(self, edges: list[list[int]], queries: list[list[int]]) -> list[int]:
        """
        Assigns edge weights to a tree such that the sum of weights along any path
        is either odd or even, and calculates the number of ways to achieve an odd sum
        for given query paths.

        Args:
            edges: A list of lists representing the edges of the tree. Each inner list [u, v]
                   denotes an edge between node u and node v.
            queries: A list of lists representing the queries. Each inner list [u, v]
                     denotes a path between node u and node v for which to calculate the result.
        Returns:
            A list of integers, where each element is the number of ways to assign weights
            such that the path sum for the corresponding query is odd, modulo 10^9 + 7.
        """
        MOD = 10 ** 9 + 7
        n = len(edges) + 1

        # Build adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Build tree with BFS from node 1 (root)
        parent = [-1] * (n + 1)
        depth = [0] * (n + 1)
        visited = [False] * (n + 1)

        queue = deque([1])
        visited[1] = True
        depth[1] = 0

        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    parent[neighbor] = node
                    depth[neighbor] = depth[node] + 1
                    queue.append(neighbor)

        # Binary lifting for LCA
        max_log = 20
        up = [[-1] * max_log for _ in range(n + 1)]

        # up[node][j] = 2^j-th ancestor of node
        for node in range(1, n + 1):
            up[node][0] = parent[node]

        for j in range(1, max_log):
            for node in range(1, n + 1):
                if up[node][j - 1] != -1:
                    up[node][j] = up[up[node][j - 1]][j - 1]

        def lca(u, v):
            # Make u the deeper node
            if depth[u] < depth[v]:
                u, v = v, u

            # Bring u to the same level as v
            diff = depth[u] - depth[v]
            for j in range(max_log):
                if (diff >> j) & 1:
                    u = up[u][j]

            if u == v:
                return u

            # Binary search for LCA
            for j in range(max_log - 1, -1, -1):
                if up[u][j] != up[v][j]:
                    u = up[u][j]
                    v = up[v][j]

            return up[u][0]

        def path_length(u, v):
            l = lca(u, v)
            return depth[u] + depth[v] - 2 * depth[l]

        # Process queries
        result = []
        for u, v in queries:
            k = path_length(u, v)
            if k == 0:
                result.append(0)
            else:
                # Number of ways to get odd sum with k edges
                # = 2^(k-1) mod MOD
                result.append(pow(2, k - 1, MOD))

        return result