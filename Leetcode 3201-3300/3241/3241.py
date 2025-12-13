# Leetcode 3241: Time Taken to Mark All Nodes
# https://leetcode.com/problems/time-taken-to-mark-all-nodes/
# Solved on 13th of December, 2025
import sys
sys.setrecursionlimit(200000)


class Solution:
    def timeTaken(self, edges: list[list[int]]) -> list[int]:
        """
        Calculates the time taken to mark all nodes starting from each node as the source.

        Args:
            edges: A list of lists representing the edges of the tree.

        Returns:
            A list of integers where result[i] is the minimum time to mark all nodes if node i is the starting node.
        """
        n = len(edges) + 1
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        subtreeMax1 = [0] * n
        subtreeMax2 = [0] * n
        up = [0] * n

        def getCost(node):
            return 1 if node % 2 != 0 else 2

        def dfsDown(u, p):
            max1 = 0
            max2 = 0

            for v in graph[u]:
                if v == p:
                    continue
                dfsDown(v, u)
                dist = subtreeMax1[v] + getCost(v)

                if dist > max1:
                    max2 = max1
                    max1 = dist
                elif dist > max2:
                    max2 = dist

            subtreeMax1[u] = max1
            subtreeMax2[u] = max2

        def dfsUp(u, p):
            for v in graph[u]:
                if v == p:
                    continue

                distFromV = subtreeMax1[v] + getCost(v)
                maxPathExcludingV = up[u]

                if distFromV == subtreeMax1[u]:
                    maxPathExcludingV = max(maxPathExcludingV, subtreeMax2[u])
                else:
                    maxPathExcludingV = max(maxPathExcludingV, subtreeMax1[u])

                up[v] = maxPathExcludingV + getCost(u)
                dfsUp(v, u)

        dfsDown(0, -1)
        dfsUp(0, -1)

        result = []
        for i in range(n):
            result.append(max(subtreeMax1[i], up[i]))

        return result