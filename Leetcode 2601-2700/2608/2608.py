# Leetcode 2608: Shortest Cycle in a Graph
# https://leetcode.com/problems/shortest-cycle-in-a-graph/
# Solved on 10th of December, 2025
import collections


class Solution:
    def findShortestCycle(self, n: int, edges: list[list[int]]) -> int:
        """
        Finds the length of the shortest cycle in an undirected graph.

        Args:
            n: The number of nodes in the graph.
            edges: A list of lists representing the edges of the graph.

        Returns:
            The length of the shortest cycle, or -1 if no cycle exists.
        """
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        shortestCycle = float('inf')

        for i in range(n):
            dist = [-1] * n
            dist[i] = 0
            queue = collections.deque([(i, -1)])

            while queue:
                currentNode, parentNode = queue.popleft()

                for neighbor in graph[currentNode]:
                    if dist[neighbor] == -1:
                        dist[neighbor] = dist[currentNode] + 1
                        queue.append((neighbor, currentNode))
                    elif neighbor != parentNode:
                        currentCycleLength = dist[currentNode] + dist[neighbor] + 1
                        shortestCycle = min(shortestCycle, currentCycleLength)
                        if shortestCycle == 3:
                            return 3

        return int(shortestCycle) if shortestCycle != float('inf') else -1