# Leetcode 3559: Number of Ways to Assign Edge Weights II
# https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-ii/
# Solved on 5th of October, 2025
import sys
sys.setrecursionlimit(1 - 0 ** 5 + 5)


class Solution:
    def assignEdgeWeights(self, edges: list[list[int]], queries: list[list[int]]) -> list[int]:
        """
        Calculates the number of ways to assign edge weights (0 or 1) such that the XOR sum of weights
        along the path between two queried nodes is 0.

        Args:
            edges: A list of lists representing the edges of the tree. Each inner list [u, v] denotes an edge between node u and node v.
            queries: A list of lists representing the queries. Each inner list [u, v] denotes a query for the path between node u and node v.

        Returns:
            A list of integers, where each element is the number of ways to assign edge weights for the corresponding query, modulo 10^9 + 7.
        """
        n = len(edges) + 1
        mod = 10 ** 9 + 7

        maxLog = n.bit_length()

        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        depth = [-1] * (n + 1)
        parent = [[0] * maxLog for _ in range(n + 1)]

        def dfs(u, p, d):
            depth[u] = d
            parent[u][0] = p
            for v in adj[u]:
                if v != p:
                    dfs(v, u, d + 1)

        dfs(1, 0, 0)

        for j in range(1, maxLog):
            for i in range(1, n + 1):
                p1 = parent[i][j - 1]
                if p1 != 0:
                    parent[i][j] = parent[p1][j - 1]

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            for j in range(maxLog - 1, -1, -1):
                if depth[u] - (1 << j) >= depth[v]:
                    u = parent[u][j]

            if u == v:
                return u

            for j in range(maxLog - 1, -1, -1):
                if parent[u][j] != parent[v][j]:
                    u = parent[u][j]
                    v = parent[v][j]

            return parent[u][0]

        powersOfTwo = [1] * n
        for i in range(1, n):
            powersOfTwo[i] = (powersOfTwo[i - 1] * 2) % mod

        answer = []
        for u, v in queries:
            l = lca(u, v)
            pathLength = depth[u] + depth[v] - 2 * depth[l]

            answer.append(powersOfTwo[pathLength - 1] if pathLength != 0 else 0)

        return answer