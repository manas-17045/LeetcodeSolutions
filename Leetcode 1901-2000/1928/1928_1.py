# Leetcode 1928: Minimum Cost to Reach Destination in Time
# https://leetcode.com/problems/minimum-cost-to-reach-destination-in-time/
# Solved on 19th of June, 2025
import heapq


class Solution:
    def minCost(self, maxTime: int, edges: list[list[int]], passingFees: list[int]) -> int:
        """
        Finds the minimum cost to reach the destination city (n-1) from city 0
        within a given maximum time.

        Args:
            maxTime: The maximum allowed time to reach the destination.
            edges: A list of edges, where each edge is represented as [u, v, time],
                   indicating a road between city u and city v that takes 'time'
                   minutes to traverse.
            passingFees: A list of integers where passingFees[i] is the fee to enter city i.

        Returns:
            The minimum cost to reach the destination within maxTime, or -1 if it's impossible.
        """
        n = len(passingFees)

        adj = [[] for _ in range(n)]
        for uNode, vNode, tEdge in edges:
            adj[uNode].append((vNode, tEdge))
            adj[vNode].append((uNode, tEdge))

        minCostAtTime = [[float('inf')] * (maxTime + 1) for _ in range(n)]
        minCostAtTime[0][0] = passingFees[0]

        pq = [(passingFees[0], 0, 0)]

        while pq:
            cost, timeVal, u = heapq.heappop(pq)

            if cost > minCostAtTime[u][timeVal]:
                continue

            for v, edgeTime in adj[u]:
                newTime = timeVal + edgeTime
                if newTime <= maxTime:
                    newCost = cost + passingFees[v]
                    if newCost < minCostAtTime[v][newTime]:
                        minCostAtTime[v][newTime] = newCost
                        heapq.heappush(pq, (newCost, newTime, v))

        destinationNode = n - 1
        finalMinCost = float('inf')

        for t in range(maxTime + 1):
            finalMinCost = min(finalMinCost, minCostAtTime[destinationNode][t])

        if finalMinCost == float('inf'):
            return -1
        else:
            return int(finalMinCost)