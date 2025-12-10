# Leetcode 2360: Longest Cycle in a Graph
# https://leetcode.com/problems/longest-cycle-in-a-graph/
# Solved on 10th of December, 2025
class Solution:
    def longestCycle(self, edges: list[int]) -> int:
        """
        Finds the length of the longest cycle in a directed graph.

        Args:
            edges: A list representing the directed graph where edges[i] is the neighbor of node i.
                   If edges[i] == -1, there is no outgoing edge from node i.
        Returns:
            The length of the longest cycle in the graph. If no cycle exists, returns -1.
        """
        maxLength = -1
        n = len(edges)
        visited = [False] * n

        for i in range(n):
            if visited[i]:
                continue

            nodeDistances = {}
            currentNode = i
            currentDistance = 0

            while currentNode != -1:
                if currentNode in nodeDistances:
                    cycleLength = currentDistance - nodeDistances[currentNode]
                    maxLength = max(maxLength, cycleLength)
                    break

                if visited[currentNode]:
                    break

                visited[currentNode] = True
                nodeDistances[currentNode] = currentDistance
                currentNode = edges[currentNode]
                currentDistance += 1

        return maxLength