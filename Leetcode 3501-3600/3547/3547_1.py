# Leetcode 3547: Maximum Sum of Edge Values in a Graph
# https://leetcode.com/problems/maximum-sum-of-edge-values-in-a-graph/
# Solved on 12th of June, 2025
from collections import deque


class Solution:
    def maxScore(self, n: int, edges: list[list[int]]) -> int:
        """
        Calculates the maximum possible sum of edge values in a graph.

        The problem asks to assign values from 1 to n to the nodes of a given
        graph such that the sum of values of adjacent nodes for each edge is
        maximized. The value of an edge (u, v) is defined as the product of
        the values assigned to nodes u and v.

        Args:
            n: The number of nodes in the graph.
            edges: A list of lists representing the edges of the graph.

        Returns:
            The maximum possible sum of edge values.
        """
        if n == 1:
            return 0

        degrees = [0] * n
        for u, v in edges:
            degrees[u] += 1
            degrees[v] += 1

        isCycle = True
        for d in degrees:
            if d == 1:
                isCycle = False
                break

        values = deque([n, (n - 1)])
        score = n * (n - 1)

        for val in range((n - 2), 0, -1):
            leftEnd = values[0]
            rightEnd = values[-1]

            if leftEnd > rightEnd:
                score += val * leftEnd
                values.appendleft(val)
            else:
                score += val * rightEnd
                values.append(val)

        if isCycle:
            score += values[0] * values[-1]

        return score