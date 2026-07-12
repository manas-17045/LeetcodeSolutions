# Leetcode 3970: Shortest Path With At Most K Consecutive Identical Characters
# https://leetcode.com/problems/shortest-path-with-at-most-k-consecutive-identical-characters/
# Solved on 12th of July, 2026
import heapq


class Solution:
    def shortestPath(self, n: int, edges: list[list[int]], labels: str, k: int) -> int:
        """
        Finds the shortest path from node 0 to node n-1 with at most k consecutive identical characters.
        
        @param n      The number of nodes.
        @param edges  The edges.
        @param labels The labels.
        @param k      The maximum number of consecutive identical characters.
        @return The shortest path.
        """
        adjList = [[] for _ in range(n)]
        for fromNode, toNode, weight in edges:
            adjList[fromNode].append((toNode, weight))

        minDist = [[float('inf')] * (k + 1) for _ in range(n)]
        minDist[0][1] = 0

        priorityQueue = [(0, 0, 1)]

        while priorityQueue:
            currDist, currNode, currCount = heapq.heappop(priorityQueue)

            if currNode == n - 1:
                return currDist

            if currDist > minDist[currNode][currCount]:
                continue

            for nextNode, edgeWeight in adjList[currNode]:
                if labels[nextNode] == labels[currNode]:
                    nextCount = currCount + 1
                else:
                    nextCount = 1

                if nextCount <= k and currDist + edgeWeight < minDist[nextNode][nextCount]:
                    minDist[nextNode][nextCount] = currDist + edgeWeight
                    heapq.heappush(priorityQueue, (currDist + edgeWeight, nextNode, nextCount))

        return -1