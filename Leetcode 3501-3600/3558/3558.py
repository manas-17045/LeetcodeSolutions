# Leetcode 33558: Number of Ways to Assign Edge Weights I
# https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-i/
# Solved on 22nd of October, 2025
import collections


class Solution:
    def assignEdgeWeights(self, edges: list[list[int]]) -> int:
        """
        Calculates the number of ways to assign edge weights such that the longest path from node 1 has a specific length.

        :param edges: A list of lists representing the edges of the tree. Each inner list [u, v] denotes an edge between node u and node v.
        :return: The number of ways to assign edge weights modulo 10^9 + 7.
        """
        adjList = collections.defaultdict(list)
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        queue = collections.deque()
        queue.append((1, 0))

        visited = set()
        visited.add(1)

        maxDepth = 0

        while queue:
            node, d = queue.popleft()
            maxDepth = max(maxDepth, d)

            for neighbor in adjList[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, d + 1))

        if maxDepth == 0:
            return 0

        pathLength = maxDepth
        modVal = 10**9 + 7

        exponent = pathLength - 1
        base = 2

        result = pow(base, exponent, modVal)
        return result