# Leetcode 3604: Minimum Time to Reach Destination in Directed Graph
# https://leetcode.com/problems/minimum-time-to-reach-destination-in-directed-graph/
# Solved on 30th of December, 2025
import heapq


class Solution:
    def minTime(self, n: int, edges: list[list[int]]) -> int:
        """
        Calculates the minimum time to reach the destination node (n-1) from the source node (0)
        in a directed graph with time-dependent edges.

        Args:
            n: The number of nodes in the graph.
            edges: A list of edges, where each edge is [u, v, start, end].
                   u: The starting node of the edge.
                   v: The ending node of the edge.
                   start: The earliest time an edge can be traversed.
                   end: The latest time an edge can be traversed.

        Returns:
            The minimum time to reach the destination node (n-1), or -1 if it's not reachable.
        """
        adjList = [[] for _ in range(n)]
        for u, v, start, end in edges:
            adjList[u].append((v, start, end))

        minArrivalTimes = [float('inf')] * n
        minArrivalTimes[0] = 0
        minHeap = [(0, 0)]

        while minHeap:
            currTime, currNode = heapq.heappop(minHeap)

            if currNode == n - 1:
                return currTime

            if currTime > minArrivalTimes[currNode]:
                continue

            for nextNode, start, end in adjList[currNode]:
                departTime = max(currTime, start)

                if departTime <= end:
                    arrivalTime = departTime + 1
                    if arrivalTime < minArrivalTimes[nextNode]:
                        minArrivalTimes[nextNode] = arrivalTime
                        heapq.heappush(minHeap, (arrivalTime, nextNode))

        return -1