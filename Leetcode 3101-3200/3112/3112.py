# Leetcode 3112: Minimum Time to Visit Disappearing Nodes
# https://leetcode.com/problems/minimum-time-to-visit-disappearing-nodes/
# Solved on 4th of January, 2026
import heapq


class Solution:
    def minimumTime(self, n: int, edges: list[list[int]], disappear: list[int]) -> list[int]:
        """
        Calculates the minimum time to visit each node from node 0, considering nodes disappear at certain times.

        Args:
            n (int): The number of nodes in the graph.
            edges (list[list[int]]): A list of edges, where each edge is [u, v, length]
                                     representing an undirected edge between nodes u and v with a given length.
            disappear (list[int]): A list where disappear[i] is the time at which node i disappears.

        Returns:
            list[int]: A list of length n, where result[i] is the minimum time to reach node i from node 0.
                       If a node cannot be reached before it disappears, the corresponding value is -1.
        """
        adjacencyList = [[] for _ in range(n)]
        for u, v, length in edges:
            adjacencyList[u].append((v, length))
            adjacencyList[v].append((u, length))

        minTimes = [float('inf')] * n
        minTimes[0] = 0
        priorityQueue = [(0, 0)]

        while priorityQueue:
            currentTime, u = heapq.heappop(priorityQueue)

            if currentTime > minTimes[u]:
                continue

            for v, length in adjacencyList[u]:
                arrivalTime = currentTime + length
                if arrivalTime < disappear[v] and arrivalTime < minTimes[v]:
                    minTimes[v] = arrivalTime
                    heapq.heappush(priorityQueue, (arrivalTime, v))

        return [-1 if t == float('inf') else t for t in minTimes]