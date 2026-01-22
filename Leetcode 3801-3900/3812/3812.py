# Leetcode 3812: Minimum Edges Toggles on a Tree
# https://leetcode.com/problems/minimum-edge-toggles-on-a-tree/
# Solved on 22nd of January, 2026
class Solution:
    def minimumFlips(self, n: int, edges: list[list[int]], start: str, target: str) -> list[int]:
        """
        Calculates the minimum set of edge indices to toggle to transform start states to target states.

        Args:
            n (int): Number of nodes in the tree.
            edges (list[list[int]]): List of edges [u, v].
            start (str): Initial binary states of nodes.
            target (str): Target binary states of nodes.

        Returns:
            list[int]: Sorted list of edge indices to toggle, or [-1] if impossible.
        """
        needsFlip = [0] * n
        mismatchCount = 0
        for i in range(n):
            if start[i] != target[i]:
                needsFlip[i] = 1
                mismatchCount += 1

        if mismatchCount % 2 != 0:
            return [-1]

        adjList = [[] for _ in range(n)]
        for index, (u, v) in enumerate(edges):
            adjList[u].append((v, index))
            adjList[v].append((u, index))

        bfsQueue = [0]
        visitOrder = []
        visited = [False] * n
        visited[0] = True
        parentMap = {}

        head = 0
        while head < len(bfsQueue):
            u = bfsQueue[head]
            head += 1
            visitOrder.append(u)

            for v, edgeIndex in adjList[u]:
                if not visited[v]:
                    visited[v] = True
                    parentMap[v] = (u, edgeIndex)
                    bfsQueue.append(v)

        resultEdges = []
        for i in range(n - 1, -1, -1):
            u = visitOrder[i]
            if u == 0:
                continue

            if needsFlip[u] == 1:
                parent, edgeIndex = parentMap[u]
                resultEdges.append(edgeIndex)
                needsFlip[parent] ^= 1

        resultEdges.sort()
        return resultEdges