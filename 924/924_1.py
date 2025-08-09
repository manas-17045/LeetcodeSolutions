# Leetcode 924: Minimize Malware Spread
# https://leetcode.com/problems/minimize-malware-spread/
# Solved on 9th of August, 2025
from collections import Counter


class Solution:
    def minMalwareSpread(self, graph: list[list[int]], initial: list[int]) -> int:
        """
        Minimizes the spread of malware by removing a single infected node.

        Args:
            graph (list[list[int]]): An adjacency matrix representing the network.
                                     graph[i][j] = 1 if node i and node j are connected, else 0.
            initial (list[int]): A list of initially infected nodes.

        Returns:
            int: The node ID that, if removed, minimizes the total number of infected nodes.
                 If multiple nodes result in the same minimum, return the smallest indexed node.
        """
        numNodes = len(graph)
        parent = list(range(numNodes))
        componentSize = [1] * numNodes

        def findSet(i):
            if parent[i] == i:
                return i
            parent[i] = findSet(parent[i])
            return parent[i]

        def uniteSets(i, j):
            rootI = findSet(i)
            rootJ = findSet(j)
            if rootI != rootJ:
                if componentSize[rootI] < componentSize[rootJ]:
                    rootI, rootJ = rootJ, rootI
                parent[rootJ] = rootI
                componentSize[rootI] += componentSize[rootJ]

        for i in range(numNodes):
            for j in range(i + 1, numNodes):
                if graph[i][j] == 1:
                    uniteSets(i, j)
        
        infectionCountPerComponent = Counter(findSet(i) for i in initial)
        
        maxSizeSaved = -1
        initial.sort()
        nodeToReturn = initial[0]
        
        for nodeToRemove in initial:
            root = findSet(nodeToRemove)
            if infectionCountPerComponent[root] == 1:
                size = componentSize[root]
                if size > maxSizeSaved:
                    maxSizeSaved = size
                    nodeToReturn = nodeToRemove
        
        return nodeToReturn