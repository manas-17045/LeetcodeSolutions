# Leetcode 1786: Number of Restricted Paths From First to Last Node
# https://leetcode.com/problems/number-of-restricted-paths-from-first-to-last-node/
# Solved on 24th of August, 2025
import collections
import heapq


class Solution:
    def countRestrictedPaths(self, n: int, edges: list[list[int]]) -> int:
        """
        Calculates the number of restricted paths from node 1 to node `n`.

        Args:
            n (int): The number of nodes in the graph.
            edges (list[list[int]]): A list of edges, where each edge is [u, v, w] representing a path between u and v with weight w.

        Returns:
            int: The number of restricted paths.
        """
        if n == 1:
            return 0

        mod = 10**9 + 7

        graph = collections.defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        distanceToLastNode = [float('inf')] * (n + 1)
        priorityQueue = [(0, n)]
        distanceToLastNode[n] = 0

        while priorityQueue:
            dist, u = heapq.heappop(priorityQueue)

            if dist > distanceToLastNode[u]:
                continue

            for v, w in graph[u]:
                if distanceToLastNode[v] > dist + w:
                    distanceToLastNode[v] = dist + w
                    heapq.heappush(priorityQueue, (distanceToLastNode[v], v))

        memo = {}
        def dfs(node):
            if node == 1:
                return 1

            if node in memo:
                return memo[node]

            ans = 0
            for neighbor, weight in graph[node]:
                if distanceToLastNode[node] > distanceToLastNode[neighbor]:
                    ans = (ans + dfs(neighbor)) % mod

            memo[node] = ans
            return ans

        return dfs(1)