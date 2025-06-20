# Leetcode 2065: Maximum Path Quality of a Graph
# https://leetcode.com/problems/maximum-path-quality-of-a-graph/
# Solved on 20th of June, 2025
import sys
sys.setrecursionlimit(10 ** 7)


class Solution:
    def maximalPathQuality(self, values: list[int], edges: list[list[int]], maxTime: int) -> int:
        """
        Calculates the maximal path quality starting and ending at node 0 within a given time limit.

        The quality of a path is the sum of the values of the unique nodes visited along the path.
        A node's value is added to the quality only the first time it is visited.

        Args:
            values: A list of integers representing the values of each node.
            edges: A list of lists, where each inner list represents an edge [u, v, time]
                   connecting nodes u and v with a travel time of time.
            maxTime: The maximum allowed time for the path.

        Returns:
            The maximal path quality achievable within the time limit.
        """
        n = len(values)
        adj = [[] for _ in range(n)]
        for u, v, t in edges:
            adj[u].append((v, t))
            adj[v].append((u, t))

        # dp[u][t] = best quality we've seen arriving at node u in exactly t time
        dp = [[-1] * (maxTime + 1) for _ in range(n)]

        visited = [False] * n
        visited[0] = True
        best = 0

        def dfs(u: int, timeSpent: int, quality: int):
            nonlocal best
            if u == 0:
                best = max(best, quality)

            for v, cost in adj[u]:
                nt = timeSpent + cost
                if nt > maxTime:
                    continue

                # If first time, we step on v, we get its value
                add = 0
                if not visited[v]:
                    add = values[v]
                nq = quality + add

                # Only prune if strictly worse than what we've already achieved
                if dp[v][nt] > nq:
                    continue

                # Record that we can achieve at least nq here
                dp[v][nt] = nq

                first_time = False
                if not visited[v]:
                    visited[v] = True
                    first_time = True

                dfs(v, nt, nq)

                if first_time:
                    visited[v] = False

        # kick off from 0
        dp[0][0] = values[0]
        dfs(0, 0, values[0])
        return best