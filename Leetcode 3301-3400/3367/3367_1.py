# Leetcode 3367: Maximize Sum of Weights after Edge Removals
# https://leetcode.com/problems/maximize-sum-of-weights-after-edge-removals/
# Solved on 13th of June, 2025
import sys
from collections import defaultdict


class Solution:
    def maximizeSumOfWeights(self, edges: list[list[int]], k: int) -> int:
        """
        Maximizes the sum of weights of remaining edges after removing exactly k edges.

        Args:
            edges: A list of edges, where each edge is represented as [u, v, weight].
            k: The number of edges to remove.

        Returns:
            The maximum possible sum of weights of the remaining edges.
        """
        sys.setrecursionlimit(len(edges) + 50)

        adjacencyList = defaultdict(list)
        for u, v, weight in edges:
            adjacencyList[u].append((v, weight))
            adjacencyList[v].append((u, weight))

        memo = {}

        def dfs(node, parent):
            if (node, parent) in memo:
                return memo[(node, parent)]

            childGains = []
            baseSum = 0

            for neighbor, weight in adjacencyList[node]:
                if neighbor == parent:
                    continue

                sumIfNeighborConnected, sumIfNeighborDisconnected = dfs(neighbor, node)

                baseSum += sumIfNeighborDisconnected
                gain = weight + sumIfNeighborConnected - sumIfNeighborDisconnected

                if gain > 0:
                    childGains.append(gain)

            childGains.sort(reverse=True)

            sumIfConnected = baseSum
            numToKeepForConnected = min(len(childGains), (k - 1))
            for i in range(numToKeepForConnected):
                sumIfConnected += childGains[i]

            sumIfDisconnected = baseSum
            numToKeepForDisconnected = min(len(childGains), k)
            for i in range(numToKeepForDisconnected):
                sumIfDisconnected += childGains[i]

            memo[(node, parent)] = (sumIfConnected, sumIfDisconnected)
            return sumIfConnected, sumIfDisconnected

        _, result = dfs(0, -1)

        return result