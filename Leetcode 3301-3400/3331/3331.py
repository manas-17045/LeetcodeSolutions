# Leetcode 3331: Find Subtree Sizes After Changes
# https://leetcode.com/problems/find-subtree-sizes-after-changes/
# Solved on 2nd of January, 2026
import sys
sys.setrecursionlimit(200000)


class Solution:
    def findSubtreeSizes(self, parent: list[int], s: str) -> list[int]:
        """
        Finds the size of each subtree after re-parenting nodes based on character occurrences.

        Args:
            parent: A list where parent[i] is the parent of node i. parent[0] is always -1.
            s: A string where s[i] is the character associated with node i.

        Returns:
            A list where subtreeSizes[i] is the size of the subtree rooted at node i
            in the modified tree structure.
        """
        n = len(parent)
        adjacencyList = [[] for _ in range(n)]
        for i in range(1, n):
            adjacencyList[parent[i]].append(i)

        newParents = list(parent)
        ancestors = [-1] * 26

        def findNewStructure(node):
            charIndex = ord(s[node]) - 97
            previousAncestor = ancestors[charIndex]

            if previousAncestor != -1:
                newParents[node] = previousAncestor

            ancestors[charIndex] = node

            for child in adjacencyList[node]:
                findNewStructure(child)

            ancestors[charIndex] = previousAncestor

        findNewStructure(0)

        finalAdjacencyList = [[] for _ in range(n)]
        for i in range(1, n):
            finalAdjacencyList[newParents[i]].append(i)

        subtreeSizes = [0] * n

        def calculateSizes(node):
            currentSize = 1
            for child in finalAdjacencyList[node]:
                currentSize += calculateSizes(child)
            subtreeSizes[node] = currentSize
            return currentSize

        calculateSizes(0)
        return subtreeSizes
