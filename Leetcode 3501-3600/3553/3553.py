# Leetcode 3553: Minimum Weighted Subgraph With the Required Paths II
# https://leetcode.com/problems/minimum-weighted-subgraph-with-the-required-paths-ii/
# Solved on 17th of December, 2025
class Solution:
    def minimumWeight(self, edges: list[list[int]], queries: list[list[int]]) -> list[int]:
        """
        Calculates the minimum weighted subgraph for a set of queries.

        Args:
            edges: A list of edges, where each edge is [u, v, w] representing an undirected edge between u and v with weight w.
            queries: A list of queries, where each query is [s1, s2, d] representing three nodes.
        Returns:
            A list of integers, where each integer is the minimum weighted subgraph for the corresponding query.
        """
        n = len(edges) + 1
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))

        depth = [0] * n
        dist = [0] * n
        parent = [0] * n
        visited = [False] * n

        queue = [0]
        visited[0] = True
        parent[0] = -1

        head = 0
        while head < len(queue):
            u = queue[head]
            head += 1
            for v, w in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    parent[v] = u
                    depth[v] = depth[u] + 1
                    dist[v] = dist[u] + w
                    queue.append(v)

        LOG = 18
        up = [[-1] * LOG for _ in range(n)]

        for i in range(n):
            up[i][0] = parent[i]

        for j in range(1, LOG):
            for i in range(n):
                if up[i][j - 1] != -1:
                    up[i][j] = up[up[i][j - 1]][j - 1]
                else:
                    up[i][j] = -1

        def getLca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            diff = depth[u] - depth[v]
            for j in range(LOG):
                if (diff >> j) & 1:
                    u = up[u][j]

            if u == v:
                return u

            for j in range(LOG - 1, -1, -1):
                if up[u][j] != up[v][j]:
                    u = up[u][j]
                    v = up[v][j]

            return up[u][0]

        result = []
        for s1, s2, d in queries:
            lca1 = getLca(s1, s2)
            lca2 = getLca(s1, d)
            lca3 = getLca(s2, d)

            dist12 = dist[s1] + dist[s2] - 2 * dist[lca1]
            dist1d = dist[s1] + dist[d] - 2 * dist[lca2]
            dist2d = dist[s2] + dist[d] - 2 * dist[lca3]

            result.append((dist12 + dist1d + dist2d) // 2)

        return result