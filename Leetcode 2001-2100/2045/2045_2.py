# Leetcode 2045: Second Minimum Time to Reach Destination
# https://leetcode.com/problems/second-minimum-time-to-reach-destination/
# Solved on 30th of May, 2025
import heapq


class Solution:
    def secondMinimum(self, n: int, edges: list[list[int]], time: int, change: int) -> int:
        """
        Finds the second minimum time to travel from node 1 to node n in a graph.

        The graph is represented by an adjacency list. The travel time between adjacent
        nodes is fixed. Traffic signals at each node alternate between green and red
        phases, each lasting 'change' minutes. A node can only be departed from during
        a green phase.

        Args:
            n: The number of nodes in the graph.
            edges: A list of edges, where each edge is a list [u, v] representing a connection between nodes u and v.
            time: The time it takes to travel between any two adjacent nodes.
            change: The duration of each green and red phase of the traffic signals.
        """

        # Build adjacency list
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        INF = float('inf')
        # first[i], second[i] = the smallest and second-smallest arrival times to node i
        first = [INF] * (n + 1)
        second = [INF] * (n + 1)

        # Min-Heap of (current_time, node)
        pq = []
        first[1] = 0
        heapq.heappush(pq, (0, 1))

        while pq:
            t, u = heapq.heappop(pq)
            # We only care about up to the second best
            if t > second[u]:
                continue
            # The first time, we pop a time > first[n], that's the second minimum
            if u == n and t > first[n]:
                return t

            # Determine when we can depart from u (may have to wait for a green signal)
            cycle = t // change
            if cycle % 2 == 1:
                # Currently in a red phase -> wait until the next green
                wait = (cycle + 1) * change - t
            else:
                wait = 0
            depart = t + wait

            # Relax edges
            for x in adj[u]:
                arrival = depart + time
                # Update first/second best for v
                if arrival < first[x]:
                    second[x] = first[x]
                    first[x] = arrival
                    heapq.heappush(pq, (arrival, x))
                elif first[x] < arrival < second[x]:
                    second[x] = arrival
                    heapq.heappush(pq, (arrival, x))

        # If there is no second minimum
        return -1