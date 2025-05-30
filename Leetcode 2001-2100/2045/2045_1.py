# Leetcode 2045: Second Minimum Time to Reach Destination
# https://leetcode.com/problems/second-minimum-time-to-reach-destination/
# Solved on 28th of July, 2024
import collections
import math


class Solution:
    def secondMinimum(self, n: int, edges: list[list[int]], time: int, change: int) -> int:
        """
        Finds the second minimum time to reach destination node n from node 1.

        Args:
            n: The number of nodes in the graph.
            edges: A list of edges, where each edge is represented as [u, v].
            time: The time taken to travel between any two adjacent nodes.
            change: The duration of each traffic light cycle.

        Returns:
            The second minimum time to reach node n, or -1 if it's not possible
            to reach node n twice.
        """

        graph = [[] for _ in range(n + 1)]
        q = collections.deque([(1, 0)])
        minTime = [[math.inf] * 2 for _ in range(n + 1)]
        minTime[1][0] = 0

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        while q:
            i, prevTime = q.popleft()
            numChangeSignal = prevTime // change
            waitTime = 0 if numChangeSignal % 2 == 0 else (change - (prevTime % change))
            newTime = prevTime + time + waitTime
            for j in graph[i]:
                if newTime < minTime[j][0]:
                    minTime[j][0] = newTime
                    q.append((j, newTime))
                elif minTime[j][0] < newTime < minTime[j][1]:
                    if j == n:
                        return newTime
                    minTime[j][1] = newTime
                    q.append((j, newTime))

        return -1