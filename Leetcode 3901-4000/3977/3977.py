# Leetcode 3977: Minimum Time to Reach Target With Limited Power
# https://leetcode.com/problems/minimum-time-to-reach-target-with-limited-power/
# Solved on 19th of July, 2026
import heapq


class Solution:
    def minTimeMaxPower(self, n: int, edges: list[list[int]], power: int, cost: list[int], source: int, target: int) -> list[int]:
        """
        Finds the minimum time to reach the target node from the source node with limited power.
        @param n The number of nodes.
        @param edges The edges.
        @param power The initial power.
        @param cost The cost to travel to each node.
        @param source The source node.
        @param target The target node.
        @return An array of two integers representing the minimum time and maximum power.
        """
        adjList = [[] for _ in range(n)]
        for u, v, t in edges:
            adjList[u].append((v, t))

        minHeap = [(0, -power, source)]
        maxPowerVisited = [-1] * n

        while minHeap:
            timeTaken, negPower, currentNode = heapq.heappop(minHeap)
            currentPower = -negPower

            if currentPower <= maxPowerVisited[currentNode]:
                continue

            maxPowerVisited[currentNode] = currentPower

            if currentNode == target:
                return [timeTaken, currentPower]

            if currentPower >= cost[currentNode]:
                nextPower = currentPower - cost[currentNode]
                for neighbor, travelTime in adjList[currentNode]:
                    heapq.heappush(minHeap, (timeTaken + travelTime, -nextPower, neighbor))

        return [-1, -1]