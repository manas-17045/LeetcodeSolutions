# Leetcode 3585: Find Weighted Median Node in Tree
# https://leetcode.com/problems/find-weighted-median-node-in-tree/
# Solved on 19th of December, 2025
import sys
sys.setrecursionlimit(200000)


class Solution:
    def findMedian(self, n: int, edges: list[list[int]], queries: list[list[int]]) -> list[int]:
        """
        Finds the weighted median node for a series of queries in a given tree.

        Args:
            n (int): The number of nodes in the tree.
            edges (list[list[int]]): A list of edges, where each edge is [u, v, w] representing an edge
                                     between nodes u and v with weight w.
            queries (list[list[int]]): A list of queries, where each query is [u, v] representing a path
                                       between nodes u and v.
        Returns:
            list[int]: A list of integers, where each integer is the weighted median node for the corresponding query.
        """
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))

        LOG = 18
        parent = [[-1] * LOG for _ in range(n)]
        depth = [0] * n
        level = [0] * n

        queue = [0]
        visited = [False] * n
        visited[0] = True

        idx = 0
        while idx < len(queue):
            u = queue[idx]
            idx += 1

            for v, w in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    depth[v] = depth[u] + w
                    level[v] = level[u] + 1
                    parent[v][0] = u
                    queue.append(v)

        for j in range(1, LOG):
            for i in range(n):
                if parent[i][j - 1] != -1:
                    parent[i][j] = parent[parent[i][j - 1]][j - 1]
                else:
                    parent[i][j] = -1

        def get_lca(u, v):
            if level[u] < level[v]:
                u, v = v, u

            diff = level[u] - level[v]
            for i in range(LOG):
                if (diff >> i) & 1:
                    u = parent[u][i]

            if u == v:
                return u

            for i in range(LOG - 1, -1, -1):
                if parent[u][i] != parent[v][i]:
                    u = parent[u][i]
                    v = parent[v][i]

            return parent[u][0]

        ans = []
        for u, v in queries:
            lca = get_lca(u, v)

            d_u = depth[u]
            d_v = depth[v]
            d_lca = depth[lca]

            total_weight = d_u + d_v - 2 * d_lca
            target = (total_weight + 1) // 2
            dist_u_lca = d_u - d_lca

            if dist_u_lca >= target:
                limit = d_u - target
                curr = u
                if depth[curr] > limit:
                    for i in range(LOG - 1, -1, -1):
                        p = parent[curr][i]
                        if p != -1 and depth[p] > limit:
                            curr = p
                    ans.append(parent[curr][0])
                else:
                    ans.append(curr)
            else:
                req_depth = target - dist_u_lca + d_lca
                curr = v
                for i in range(LOG - 1, -1, -1):
                    p = parent[curr][i]
                    if p != -1 and depth[p] >= req_depth:
                        curr = p
                ans.append(curr)

        return ans