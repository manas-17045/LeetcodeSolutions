# Leetcode 3650: Minimum Cost Path with Edge Reversals
# https://leetcode.com/problems/minimum-cost-path-with-edge-reversals/
# Solved on 28th of December, 2025
import heapq


class Solution:
    def minCost(self, n: int, edges: list[list[int]]) -> int:
        """
        Calculates the minimum cost to travel from node 0 to node n-1 in a graph.
        Edges can be traversed in their original direction with a given weight,
        or reversed with double the weight.
        :param n: The number of nodes in the graph.
        :param edges: A list of edges, where each edge is [u, v, w] representing
                      a directed edge from u to v with weight w.
        :return: The minimum cost to reach node n-1 from node 0, or -1 if unreachable.
        """
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, 2 * w))

        priorityQueue = [(0, 0)]
        distances = [float('inf')] * n
        distances[0] = 0

        while priorityQueue:
            currentCost, u = heapq.heappop(priorityQueue)

            if currentCost > distances[u]:
                continue

            if u == n - 1:
                return currentCost

            for v, weight in graph[u]:
                newCost = currentCost + weight
                if newCost < distances[v]:
                    distances[v] = newCost
                    heapq.heappush(priorityQueue, (newCost, v))

        return -1