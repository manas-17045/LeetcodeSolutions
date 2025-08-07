# Leetcode 882: Reachable Nodes In Subdivided Graph
# https://leetcode.com/problems/reachable-nodes-in-subdivided-graph/
# Solved on 7th of August, 2025
import heapq


class Solution:
    def reachableNodes(self, edges: list[list[int]], maxMoves: int, n: int) -> int:
        """
        Calculates the total number of reachable nodes (original and subdivided) within a given number of moves.

        Args:
            edges: A list of edges, where each edge is [u, v, cnt], representing a connection
                   between nodes u and v with cnt subdivided nodes between them.
            maxMoves: The maximum number of moves allowed.
            n: The total number of original nodes.

        Returns:
            The total count of reachable nodes.
        """

        # Build the original graph: each edge has total “length” = cnt + 1
        graph = [[] for _ in range(n)]
        for u, v, cnt in edges:
            w = cnt + 1
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        # Dijkstra from node 0
        dist = [float('inf')] * n
        dist[0] = 0
        pq = [(0, 0)]  # (distance, node)
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]:
                continue
            # Early exit if even the smallest next d exceeds maxMoves
            if d > maxMoves:
                break
            for v, w in graph[u]:
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(pq, (nd, v))
        
        # Count original nodes reachable within maxMoves
        reachable_original = sum(1 for d in dist if d <= maxMoves)
        
        # For each edge, count how many of its subdivided nodes are reached
        # by contributions from u and v without double-counting
        reach_subdivs = 0
        for u, v, cnt in edges:
            # Moves left after reaching u / v
            rem_u = max(0, maxMoves - dist[u])
            rem_v = max(0, maxMoves - dist[v])
            # We can reach at most cnt internal nodes on this edge,
            # but contributions from both ends add up
            reach_subdivs += min(cnt, rem_u + rem_v)
        
        return reachable_original + reach_subdivs