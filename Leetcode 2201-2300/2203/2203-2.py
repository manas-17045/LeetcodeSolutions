# Leetcode 2203: Minimum Weighted Subgraph With the Required Paths
# https://leetcode.com/problems/minimum-weighted-subgraph-with-the-required-paths/
# Solved on 14th of September, 2025
import heapq


class Solution:
    def minimumWeight(self, n: int, edges: list[list[int]], src1: int, src2: int, dest: int) -> int:
        """
        Calculates the minimum weight path from two source nodes (src1, src2) to a destination node (dest)
        such that the paths from src1 and src2 meet at some intermediate node 'i' and then proceed to 'dest'.

        :param n: The number of nodes in the graph.
        :param edges: A list of lists representing the edges, where each inner list is [u, v, w]
                      meaning an edge from node u to node v with weight w.
        :param src1: The first source node.
        :param src2: The second source node.
        :param dest: The destination node.
        :return: The minimum total weight of such a path, or -1 if no such path exists.
        """
        INF = 10**30

        # Build adjacency lists: forward and reversed
        g = [[] for _ in range(n)]
        gr = [[] for _ in range(n)]
        for u, v, w in edges:
            g[u].append((v, w))
            gr[v].append((u, w))

        def dijkstra(start: int, graph: list[list[tuple]]) -> list[int]:
            dist = [INF] * n
            dist[start] = 0
            heap = [(0, start)]
            while heap:
                d, u = heapq.heappop(heap)
                if d != dist[u]:
                    continue
                for v, w in graph[u]:
                    nd = d + w
                    if nd < dist[v]:
                        dist[v] = nd
                        heapq.heappush(heap, (nd, v))

            return dist

        d1 = dijkstra(src1, g)
        d2 = dijkstra(src2, g)
        d3 = dijkstra(dest, gr)

        ans = INF
        for i in range(n):
            total = d1[i] + d2[i] + d3[i]
            if total < ans:
                ans = total

        return -1 if ans >= INF else ans