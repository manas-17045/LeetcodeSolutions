# Leetcode 2846: Minimum Edge Weight Equilibrium Queries in a Tree
# https://leetcode.com/problems/minimum-edge-weight-equilibrium-queries-in-a-tree/
# Solved on 24th of June, 2025
class Solution:
    def minOperationsQueries(self, n: int, edges: list[list[int]], queries: list[list[int]]) -> list[int]:
        """
        Calculates the minimum operations required to make all edge weights on the path between two nodes
        the same for a given set of queries.

        The problem asks us to find the minimum number of operations to make all edge weights on the path
        between two nodes `u` and `v` identical. An operation consists of changing an edge's weight.
        This is equivalent to finding the most frequent edge weight on the path and then subtracting
        its count from the total path length.

        The solution uses a combination of graph traversal (DFS/BFS), binary lifting for LCA (Lowest Common Ancestor),
        and prefix sums (or cumulative counts) to efficiently calculate edge weight frequencies on paths.

        Args:
            n (int): The number of nodes in the tree.
            edges (list[list[int]]): A list of edges, where each edge is [u, v, w] representing an edge
                                     between node u and node v with weight w.
            queries (list[list[int]]): A list of queries, where each query is [u, v] representing a pair
                                       of nodes for which to calculate the minimum operations.
        Returns:
            list[int]: A list of integers, where each integer is the minimum operations for the corresponding query.
        """
        # Maximum weight label
        K = 26
        # Number of levels for binary lifting - ceil(log2(n))
        LOG = max(1, n.bit_length())

        # Build adjacency list
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        jump = [[0] * LOG for _ in range(n)]
        depth = [0] * n
        count = [[0] * (K + 1) for _ in range(n)]

        stack = [(0, -1)]
        while stack:
            u, p = stack.pop()
            for v, w in graph[u]:
                if v == p:
                    continue
                depth[v] = depth[u] + 1
                jump[v][0] = u
                cntv = count[u].copy()
                cntv[w] += 1
                count[v] = cntv
                stack.append((v, u))

        # ---Build full jump table---
        for j in range(1, LOG):
            for i in range(n):
                jump[i][j] = jump[jump[i][j - 1]][j - 1]

        # LCA by binary lifting
        def lca(u: int, v: int) -> int:
            if depth[u] > depth[v]:
                u, v = v, u
            # Lift v up to depth[u]
            diff = depth[v] - depth[u]
            for b in range(LOG):
                if diff >> b & 1:
                    v = jump[v][b]
            if u == v:
                return u
            # Lift both until just below LCA
            for b in range((LOG - 1), -1, -1):
                if jump[u][b] != jump[v][b]:
                    u = jump[u][b]
                    v = jump[v][b]
            return jump[u][0]

        # Process queries
        ans = []
        for u, v in queries:
            w = lca(u, v)
            pathLen = depth[u] + depth[v] - (2 * depth[w])
            cnt_u, cnt_v, cnt_w = count[u], count[v], count[w]
            best = 0
            for c in range(1, (K + 1)):
                freq = cnt_u[c] + cnt_v[c] - (2 * cnt_w[c])
                if freq > best:
                    best = freq
            ans.append(pathLen - best)
        return ans