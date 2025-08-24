# Leetcode 2192: All Ancestors of a Node in a Directed Acyclic Graph
# https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/
# Resolved on 24th of August, 2025
from collections import deque


class Solution:
    def getAncestors(self, n: int, edges: list[list[int]]) -> list[list[int]]:
        """
        Given a directed acyclic graph (DAG) with n nodes labeled from 0 to n - 1,
        and an array of edges where edges[i] = [fromi, toi] indicates that there is a
        unidirectional edge from fromi to toi.
        Return a list of lists answer, where answer[i] is the list of all ancestors of node i,
        sorted in ascending order.
        An ancestor of a node x is any node y such that there is a path from y to x.
        """
        revAdj = [[] for _ in range(n)]
        for fromNode, toNode in edges:
            revAdj[toNode].append(fromNode)

        ancestorsList = []
        for i in range(n):
            queue = deque(revAdj[i])
            visited = set(revAdj[i])

            while queue:
                currentNode = queue.popleft()
                for parent in revAdj[currentNode]:
                    if parent not in visited:
                        visited.add(parent)
                        queue.append(parent)

            ancestorsList.append(sorted(list(visited)))

        return ancestorsList