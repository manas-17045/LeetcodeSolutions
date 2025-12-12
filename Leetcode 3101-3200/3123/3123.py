# Leetcode 3123: Find Edges in Shortest Paths
# https://leetcode.com/problems/find-edges-in-shortest-paths/
# Solved on 12th of December, 2025
import heapq
import math


class Solution:
    def findAnswer(self, n: int, edges: list[list[int]]) -> list[bool]:
        """
        Finds all edges that are part of at least one shortest path from node 0 to node n-1.

        Args:
            n (int): The number of nodes in the graph.
            edges (list[list[int]]): A list of edges, where each edge is [u, v, w] representing an undirected edge between u and v with weight w.
        Returns:
            list[bool]: A list of booleans, where the i-th element is True if the i-th edge in the input `edges` list is part of a shortest path, and False otherwise.
        """
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        def dijkstra(startNode):
            distances = [math.inf] * n
            distances[startNode] = 0
            priorityQueue = [(0, startNode)]

            while priorityQueue:
                currentDist, currentNode = heapq.heappop(priorityQueue)

                if currentDist > distances[currentNode]:
                    continue

                for neighbor, weight in graph[currentNode]:
                    if distances[currentNode] + weight < distances[neighbor]:
                        distances[neighbor] = distances[currentNode] + weight
                        heapq.heappush(priorityQueue, (distances[neighbor], neighbor))

            return distances

        distFromSource = dijkstra(0)
        distFromTarget = dijkstra(n - 1)

        minPathSum = distFromSource[n - 1]
        answer = []

        if minPathSum == math.inf:
            return [False] * len(edges)

        for u, v, w in edges:
            isShortest = False
            if distFromSource[u] + w + distFromTarget[v] == minPathSum:
                isShortest = True
            elif distFromSource[v] + w + distFromTarget[u] == minPathSum:
                isShortest = True
            answer.append(isShortest)

        return answer