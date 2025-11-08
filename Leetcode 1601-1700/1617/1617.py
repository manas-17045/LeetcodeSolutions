# Leetcode 1617: Count Subtrees With Max Distance Between Cities
# https://leetcode.com/problems/count-subtrees-with-max-distance-between-cities/
# Solved on 8th of November, 2025
import collections


class Solution:
    def countSubgraphsForEachDiameter(self, n: int, edges: list[list[int]]) -> list[int]:
        """
        Counts the number of subgraphs for each possible diameter.

        Args:
            n: The number of cities.
            edges: A list of edges representing the connections between cities.
        Returns:
            A list where the i-th element is the number of subgraphs with diameter i+1.
        """
        adj = [[] for _ in range(n)]
        edgeList = []
        for u, v in edges:
            u -= 1
            v -= 1
            adj[u].append(v)
            adj[v].append(u)
            edgeList.append((u, v))

        dist = [[0] * n for _ in range(n)]

        for i in range(n):
            queue = collections.deque([(i, 0)])
            visited = [-1] * n
            visited[i] = 0

            while queue:
                u, d = queue.popleft()
                dist[i][u] = d
                for v in adj[u]:
                    if visited[v] == -1:
                        visited[v] = d + 1
                        queue.append((v, d + 1))

        result = [0] * (n - 1)

        for mask in range(1, 1 << n):
            nodesInMask = []
            numNodes = 0
            for i in range(n):
                if (mask >> i) & 1:
                    nodesInMask.append(i)
                    numNodes += 1

            if numNodes < 2:
                continue

            numEdges = 0
            for u, v in edgeList:
                if ((mask >> u) & 1) and ((mask >> v) & 1):
                    numEdges += 1

            if numEdges != numNodes - 1:
                continue

            maxDiameter = 0
            for i in range(numNodes):
                for j in range(i + 1, numNodes):
                    node1 = nodesInMask[i]
                    node2 = nodesInMask[j]
                    maxDiameter = max(maxDiameter, dist[node1][node2])

            if maxDiameter > 0:
                result[maxDiameter - 1] += 1

        return result