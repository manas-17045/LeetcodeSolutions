# Leetcode 2493: Divide Nodes Into the Maximum Number of Groups
# https://leetcode.com/problems/divide-nodes-into-the-maximum-number-of-groups/
# Solved on 10th of December, 2025
import collections


class Solution:
    def magnificientSets(self, n: int, edges: list[list[int]]) -> int:
        """
        Calculates the maximum number of groups nodes can be divided into such that
        no two adjacent nodes are in the same group.
        :param n: The number of nodes in the graph.
        :param edges: A list of lists representing the edges in the graph.
        :return: The maximum number of groups, or -1 if the graph is not bipartite.
        """
        adjList = [[] for _ in range(n + 1)]
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        visited = set()
        totalGroups = 0

        for i in range(1, n + 1):
            if i in visited:
                continue

            componentNodes = []
            queue = collections.deque([i])
            colors = {i: 0}
            componentNodes.append(i)
            visited.add(i)

            while queue:
                u = queue.popleft()
                for v in adjList[u]:
                    if v in colors:
                        if colors[v] == colors[u]:
                            return -1
                    else:
                        colors[v] = 1 - colors[u]
                        visited.add(v)
                        componentNodes.append(v)
                        queue.append(v)

            maxComponentGroups = 0
            for startNode in componentNodes:
                depthQueue = collections.deque([(startNode, 1)])
                depthVisited = {startNode}
                maxDepth = 1

                while depthQueue:
                    node, depth = depthQueue.popleft()
                    maxDepth = max(maxDepth, depth)

                    for neighbor in adjList[node]:
                        if neighbor not in depthVisited:
                            depthVisited.add(neighbor)
                            depthQueue.append((neighbor, depth + 1))

                maxComponentGroups = max(maxComponentGroups, maxDepth)

            totalGroups += maxComponentGroups

        return totalGroups