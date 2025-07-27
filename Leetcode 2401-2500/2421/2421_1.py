# Leetcode 2421: Number of Good Paths
# https://leetcode.com/problems/number-of-good-paths/
# Solved on 27th of July, 2025
import collections


class Solution:
    def numberOfGoodPaths(self, vals: list[int], edges: list[list[int]]) -> int:
        """
        Calculates the number of good paths in a tree.

        A path is "good" if:
        1. The starting node and the ending node have the same value.
        2. All intermediate nodes in the path have values less than or equal to the starting node's value.

        Args:
            vals (list[int]): A list of integer values for each node in the tree.
            edges (list[list[int]]): A list of edges, where each edge `[u, v]` represents an undirected connection between nodes `u` and `v`.
        Returns:
            int: The total number of good paths in the tree.
        """
        n = len(vals)
        adjList = collections.defaultdict(list)
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        valToNodes = collections.defaultdict(list)
        for i, val in enumerate(vals):
            valToNodes[val].append(i)

        parent = list(range(n))
        componentSize = [1] * n

        def findSet(i: int) -> int:
            if parent[i] == i:
                return i
            parent[i] = findSet(parent[i])
            return parent[i]

        def unionSets(i: int, j: int):
            rootI = findSet(i)
            rootJ = findSet(j)
            if rootI != rootJ:
                if componentSize[rootI] < componentSize[rootJ]:
                    rootI, rootJ = rootJ, rootI
                parent[rootJ] = rootI
                componentSize[rootI] += componentSize[rootJ]

        numGoodPaths = n

        sortedValues = sorted(valToNodes.keys())

        for val in sortedValues:
            nodesOfVal = valToNodes[val]

            for node in nodesOfVal:
                for neighbor in adjList[node]:
                    if vals[neighbor] <= vals[node]:
                        unionSets(node, neighbor)

            componentCounts = collections.defaultdict(int)
            for node in nodesOfVal:
                root = findSet(node)
                componentCounts[root] += 1

            for count in componentCounts.values():
                numGoodPaths += count * (count - 1) // 2

        return numGoodPaths