# Leetcode 3203: Find Minimum Diameter After Merging Two Trees
# https://leetcode.com/problems/find-minimum-diameter-after-merging-two-trees
# Solved on 24th of December, 2024
from collections import defaultdict


class Solution:
    def maxDepth(self, graph, u, prev, maxDiameter):
        maxSubDepth1 = 0
        maxSubDepth2 = 0
        for v in graph[u]:
            if v == prev:
                continue
            maxSubDepth = self.maxDepth(graph, v, u, maxDiameter)
            if maxSubDepth > maxSubDepth1:
                maxSubDepth2 = maxSubDepth1
                maxSubDepth1 = maxSubDepth
            elif maxSubDepth > maxSubDepth2:
                maxSubDepth2 = maxSubDepth
        maxDiameter[0] = max(maxDiameter[0], maxSubDepth1 + maxSubDepth2)
        return 1 + maxSubDepth1

    def getDiameter(self, edges):
        n = len(edges) + 1
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        maxDiameter = [0]
        self.maxDepth(graph, 0, -1, maxDiameter)
        return maxDiameter[0]

    # Main function
    def minimumDiameterAfterMerge(self, edges1: list[list[int]], edges2: list[list[int]]) -> int:
        """
        Finds the minimum possible diameter of a tree formed by merging two given trees.

        The merging operation involves connecting one node from the first tree to one node
        from the second tree with a new edge. The goal is to find the minimum diameter
        among all possible merging operations.

        Args:
            edges1: A list of edges representing the first tree.
            edges2: A list of edges representing the second tree.

        Returns:
            The minimum diameter of the merged tree.
        """
        diameter1 = self.getDiameter(edges1)
        diameter2 = self.getDiameter(edges2)
        combinedDiameter = (diameter1 + 1) // 2 + (diameter2 + 1) // 2 + 1
        return max(diameter1, diameter2, combinedDiameter)