# Leetcode 1928: Minimum Cost to Reach Destination in Time
# https://leetcode.com/problems/minimum-cost-to-reach-destination-in-time/
# Solved on 19th of June, 2025
import heapq


class Solution:
    def minCost(self, maxTime: int, edges: list[list[int]], passingFees: list[int]) -> int:
        """
        Finds the minimum cost to reach the last city (n-1) from city 0 within a given maximum time.

        Args:
            maxTime: The maximum allowed time to reach the destination.
            edges: A list of edges, where each edge is [u, v, time], representing a road
                   between city u and city v that takes 'time' minutes to travel.
            passingFees: A list where passingFees[i] is the fee to enter city i.

        Returns:
            The minimum cost to reach the last city within maxTime.
            Returns -1 if it's impossible to reach the last city within maxTime.

        Uses Dijkstra's algorithm with a priority queue, where the priority is the total fee.
        The state in the DP table and priority queue is (fee, time, node).
        """
        n = len(passingFees)
        # Build adjacency list: graph[u] = list of (v, time_cost)
        graph = [[] for _ in range(n)]
        for u, v, t in edges:
            graph[u].append((v, t))
            graph[v].append((u, t))

        # dp[node][t] = minimum fee to reach 'node' in exactly t minutes
        INF = 10**18
        dp = [[INF] * (maxTime + 1) for _ in range(n)]
        dp[0][0] = passingFees[0]

        # Min-Heap on (fee_so_far, time_so_far, node)
        pq = [(passingFees[0], 0, 0)]

        while pq:
            fee, t, u, = heapq.heappop(pq)
            # If this state is stale, skip
            if fee > dp[u][t]:
                continue

            # If we've reached destination, this is the cheapest possible
            if u == n - 1:
                return fee
            # Try all neighboring roads
            for v, travel in graph[u]:
                nt = t + travel
                if nt > maxTime:
                    continue
                nf = fee + passingFees[v]
                # If we found a cheaper way to get to v in exactly nt minutes, take it
                if nf < dp[v][nt]:
                    dp[v][nt] = nf
                    heapq.heappush(pq, (nf, nt, v))

        # o valid path within maxTime
        return -1