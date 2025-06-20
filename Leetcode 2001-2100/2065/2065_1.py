# Leetcode 2065: Maximum Path Quality of a Graph
# https://leetcode.com/problems/maximum-path-quality-of-a-graph/
# Solved on 20th of June, 2025

class Solution:
    def dfsHelper(self, u: int, currentTime: int, currentPathQuality: int, values: list[int], adj: list[list[tuple[int, int]]], maxTime: int) -> int:
        isFirstVisitInPath = (self.pathNodesCount[u] == 0)
        self.pathNodesCount[u] += 1

        newPathQuality = currentPathQuality
        if isFirstVisitInPath:
            newPathQuality += values[u]

        if u == 0:
            self.maxQuality = max(self.maxQuality, newPathQuality)

        for vNode, timeToReachV in adj[u]:
            if currentTime + timeToReachV <= maxTime:
                self.dfsHelper(vNode, (currentTime + timeToReachV), newPathQuality, values, adj, maxTime)

        self.pathNodesCount[u] -= 1

    def maximalPathQuality(self, values: list[int], edges: list[list[int]], maxTime: int) -> int:
        """
        Calculates the maximum path quality of a graph.

        Args:
            values: A list of integers representing the value of each node.
            edges: A list of lists representing the edges of the graph, where each edge is [u, v, time].
            maxTime: The maximum time allowed for a path.

        Returns:
            The maximum path quality.
        """
        n = len(values)
        adj: list[list[tuple[int, int]]] = [[] for _ in range(n)]
        for uVal, vVal, timeVal in edges:
            adj[uVal].append((vVal, timeVal))
            adj[vVal].append((uVal, timeVal))

        self.maxQuality = 0
        self.pathNodesCount = [0] * n

        self.dfsHelper(0, 0, 0, values, adj, maxTime)

        return self.maxQuality