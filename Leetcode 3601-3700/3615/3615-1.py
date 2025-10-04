# Leetcode 3615: Longest Palindromic Path in Graph
# https://leetcode.com/problems/longest-palindromic-path-in-graph/
# Solved on 4th of October, 2025
import collections


class Solution:
    def maxLen(self, n: int, edges: list[list[int]], label: str) -> int:
        """
        Finds the length of the longest palindromic path in a given graph.

        Args:
            n (int): The number of nodes in the graph.
            edges (list[list[int]]): A list of edges, where each edge is [u, v].
            label (str): A string where label[i] is the character label of node i.
        Returns:
            int: The length of the longest palindromic path.
        """
        if n == 0:
            return 0

        adjList = [[] for _ in range(n)]
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        queue = collections.deque()
        visited = set()
        maxLength = 1

        # Base case: paths of length 1
        for i in range(n):
            mask = 1 << i
            state = (i, i, mask)
            queue.append(state)
            visited.add(state)

        # Base case: paths of length 2
        for u in range(n):
            for v in adjList[u]:
                if u < v and label[u] == label[v]:
                    mask = (1 << u) | (1 << v)
                    state = (u, v, mask)
                    if state not in visited:
                        queue.append(state)
                        visited.add(state)
                        maxLength = max(maxLength, 2)

        while queue:
            u, v, currentMask = queue.popleft()

            for uNeighbor in adjList[u]:
                if (currentMask >> uNeighbor) & 1:
                    continue

                for vNeighbor in adjList[v]:
                    if (currentMask >> vNeighbor) & 1:
                        continue

                    if uNeighbor == vNeighbor:
                        continue

                    if label[uNeighbor] == label[vNeighbor]:
                        newMask = currentMask | (1 << uNeighbor) | (1 << vNeighbor)

                        newU, newV = min(uNeighbor, vNeighbor), max(uNeighbor, vNeighbor)
                        newState = (newU, newV, newMask)

                        if newState not in visited:
                            visited.add(newState)
                            queue.append((newU, newV, newMask))
                            pathLength = bin(newMask).count('1')
                            maxLength = max(maxLength, pathLength)

        return maxLength