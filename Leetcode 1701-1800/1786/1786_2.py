# Leetcode 1786: Number of Restricted Paths From First to Last Node
# https://leetcode.com/problems/number-of-restricted-paths-from-first-to-last-node/
# Solved on 24th of August, 2025
import heapq


class Solution:
    def countRestrictedPaths(self, n: int, edges: list[list[int]]) -> int:
        """
        Counts the number of restricted paths from node 1 to node n.
        A restricted path is a path such that for any two consecutive nodes u and v in the path,
        dist(u, n) > dist(v, n), where dist(x, n) is the shortest distance from x to n.

        :param n: The number of nodes in the graph.
        :param edges: A list of edges, where each edge is [u, v, w] representing an undirected edge between u and v with weight w.
        :return: The number of restricted paths from node 1 to node n, modulo 10^9 + 7.
        """
        MOD = 10 ** 9 + 7

        # Build adjacency list
        adj = [[] for _ in range(n + 1)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))

        # Dijkstra from target node n to compute shortest distances to node n
        INF = 10 ** 18
        dist = [INF] * (n + 1)
        dist[n] = 0
        heap = [(0, n)]
        while heap:
            d, u = heapq.heappop(heap)
            if d > dist[u]:
                continue
            for v, w in adj[u]:
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(heap, (nd, v))

        # Process nodes in increasing order of dist so that when we compute ways[u]
        nodes = list(range(1, n + 1))
        nodes.sort(key=lambda x: dist[x])

        ways = [0] * (n + 1)
        ways[n] = 1

        for u in nodes:
            # For each neighbor v with strictly smaller distance, add ways[v] to ways[u]
            for v, _ in adj[u]:
                if dist[u] > dist[v]:
                    ways[u] = (ways[u] + ways[v]) % MOD

        return ways[1] % MOD