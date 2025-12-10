# Leetcode 1489: Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree
# https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/
# Solved on 10th of December, 2025
class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: list[list[int]]) -> list[list[int]]:
        """
        Finds critical and pseudo-critical edges in a Minimum Spanning Tree (MST).

        A critical edge is an edge whose removal increases the MST weight.
        A pseudo-critical edge is an edge that can be part of some MST but not all MSTs.

        Args:
            n: The number of nodes in the graph.
            edges: A list of edges, where each edge is [u, v, weight].
        Returns:
            A list containing two lists: [critical_edges, pseudo_critical_edges].
            Each inner list contains the original indices of the respective edges.
        """
        for i, edge in enumerate(edges):
            edge.append(i)

        edges.sort(key=lambda x: x[2])

        def getMST(blockIdx, forceIdx):
            parent = list(range(n))

            def find(i):
                if parent[i] != i:
                    parent[i] = find(parent[i])
                return parent[i]

            def union(i, j):
                rootI = find(i)
                rootJ = find(j)
                if rootI != rootJ:
                    parent[rootI] = rootJ
                    return True
                return False

            mstWeight = 0
            edgesCount = 0

            if forceIdx != -1:
                u, v, w, _ = edges[forceIdx]
                if union(u, v):
                    mstWeight += w
                    edgesCount += 1

            for i in range(len(edges)):
                if i == blockIdx or i == forceIdx:
                    continue

                u, v, w, _ = edges[i]
                if union(u, v):
                    mstWeight += w
                    edgesCount += 1

            if edgesCount == n - 1:
                return mstWeight
            return float('inf')

        stdWeight = getMST(-1, -1)
        criticalEdges = []
        pseudoCriticalEdges = []

        for i in range(len(edges)):
            if getMST(i, -1) > stdWeight:
                criticalEdges.append(edges[i][3])
            elif getMST(-1, i) == stdWeight:
                pseudoCriticalEdges.append(edges[i][3])

        return [criticalEdges, pseudoCriticalEdges]