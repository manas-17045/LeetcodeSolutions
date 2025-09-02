# Leetcode 2368: Reachable Nodes With Restrictions
# https://leetcode.com/problems/reachable-nodes-with-restrictions/
# Solved on 2nd of September, 2025
import collections


class Solution:
    def reachableNodes(self, n: int, edges: list[list[int]], restricted: list[int]) -> int:
        """
        Given a graph represented by n nodes and a list of edges, and a list of restricted nodes,
        return the number of reachable nodes from node 0, excluding restricted nodes.
        :param n: The number of nodes in the graph.
        :param edges: A list of lists representing the edges of the graph.
        :param restricted: A list of restricted nodes that cannot be visited.
        :return: The number of reachable nodes from node 0, excluding restricted nodes.
        """
        adjList = [[] for _ in range(n)]
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        restrictedNodes = set(restricted)

        q = collections.deque()
        visitedNodes = set()

        if 0 not in restrictedNodes:
            q.append(0)
            visitedNodes.add(0)

        while q:
            node = q.popleft()

            for neighbor in adjList[node]:
                if neighbor not in restrictedNodes and neighbor not in visitedNodes:
                    visitedNodes.add(neighbor)
                    q.append(neighbor)

        return len(visitedNodes)