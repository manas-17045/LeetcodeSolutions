# Leetcode 1719: Number of Ways To Reconstruct a Tree
# https://leetcode.com/problems/number-of-ways-to-reconstruct-a-tree/
# Solved on 18th of September, 2025
import collections


class Solution:
    def checkWays(self, pairs: list[list[int]]) -> int:
        """
        Determines the number of ways to reconstruct a tree given a list of parent-child pairs.

        Args:
            pairs: A list of lists, where each inner list [u, v] represents a pair of nodes
                   (u, v) such that u is an ancestor of v or v is an ancestor of u.
        Returns:
            An integer representing the number of ways to reconstruct the tree:
            - 0 if no such tree can be reconstructed.
            - 1 if exactly one such tree can be reconstructed.
            - 2 if multiple such trees can be reconstructed (specifically, if there's ambiguity
              in parent-child relationships for nodes with the same degree).
        """
        adjacencyList = collections.defaultdict(set)
        allNodes = set()

        for u, v in pairs:
            adjacencyList[u].add(v)
            adjacencyList[v].add(u)
            allNodes.add(u)
            allNodes.add(v)

        numNodes = len(allNodes)
        nodeDegrees = {node: len(adjacencyList[node]) for node in allNodes}

        rootNode = -1
        for node in allNodes:
            if nodeDegrees[node] == numNodes - 1:
                rootNode = node
                break

        if rootNode == -1:
            return 0

        sortedNodes = sorted(list(allNodes), key=lambda x: nodeDegrees[x], reverse=True)

        result = 1

        for i in range(1, numNodes):
            childNode = sortedNodes[i]

            currentParent = -1
            minParentDegree = float('inf')

            for neighbor in adjacencyList[childNode]:
                if nodeDegrees[neighbor] >= nodeDegrees[childNode] and nodeDegrees[neighbor] < minParentDegree:
                    currentParent = neighbor
                    minParentDegree = nodeDegrees[neighbor]

            if currentParent == -1:
                return 0

            parentNode = currentParent

            for neighbor in adjacencyList[childNode]:
                if neighbor != parentNode and neighbor not in adjacencyList[parentNode]:
                    return 0

            if nodeDegrees[childNode] == nodeDegrees[parentNode]:
                result = 2

        return result