# Leetcode 2846: Minimum Edge Weight Equilibrium Queries in a Tree
# https://leetcode.com/problems/minimum-edge-weight-equilibrium-queries-in-a-tree/
# Solved on 24th of June, 2025
from collections import deque


class Solution:
    def minOperations(
            self,
            n: int,
            edges: list[list[int]],
            queries: list[list[int]]
    ) -> list[int]:
        """
        Calculates the minimum operations to make all edge weights on a path between two nodes equal.

        The problem asks to find the minimum number of operations to make all edge weights on a given path
        from `u` to `v` equal to some value `x`. This is equivalent to finding the most frequent edge weight
        `x` on that path and changing all other edge weights to `x`. The number of operations will be
        `total_edges_on_path - count_of_most_frequent_weight`.

        This solution uses Binary Lifting (LCA) to efficiently find the path between two nodes and
        precomputes path counts for each edge weight from the root to every node.

        Args:
            n (int): The number of nodes in the tree.
            edges (list[list[int]]): A list of edges, where each edge is [u, v, w] representing an edge between u and v with weight w.
            queries (list[list[int]]): A list of queries, where each query is [u, v] representing a path between u and v.

        Returns:
            list[int]: A list of integers, where each integer is the minimum operations for the corresponding query.
        """
        MAX_WEIGHT = 26

        if n == 0:
            return []
        if n == 1:
            LOGN = 1
        else:
            LOGN = (n - 1).bit_length()
            if LOGN == 0:
                LOGN = 1

        adj = [[] for _ in range(n)]
        for uVal, vVal, wVal in edges:
            adj[uVal].append((vVal, wVal))
            adj[vVal].append((uVal, wVal))

        depth = [0] * n
        up = [[-1] * LOGN for _ in range(n)]
        pathCounts = [[0] * (MAX_WEIGHT + 1) for _ in range(n)]

        bfsQueue = deque()

        depth[0] = 0
        bfsQueue.append(0)

        while bfsQueue:
            uNode = bfsQueue.popleft()

            for vNode, edgeWeight in adj[uNode]:
                if vNode == up[uNode][0]:
                    continue

                depth[vNode] = depth[uNode] + 1
                up[vNode][0] = uNode

                # Copy pathCounts from parent and update for the current edge
                for iW in range(1, (MAX_WEIGHT + 1)):
                    pathCounts[vNode][iW] = pathCounts[uNode][iW]
                pathCounts[vNode][edgeWeight] += 1

                bfsQueue.append(vNode)

        # Fill the rest of the binary lifting table "up"
        for j in range(1, LOGN):
            for iNode in range(n):
                parentHalfway = up[iNode][j - 1]
                if parentHalfway != -1:
                    up[iNode][j] = up[parentHalfway][j - 1]

        # LCA function
        def getLCA(uNode, vNode):
            if depth[uNode] < depth[vNode]:
                uNode, vNode = vNode, uNode

            # Lift uNode to the same depth as vNode
            for j in range(LOGN - 1, -1, -1):
                # Check if (2^j)-th ancestor exists and is still at or below uNode's original path to vNode's depth
                if up[uNode][j] != -1 and depth[up[uNode][j]] >= depth[vNode]:
                    uNode = up[uNode][j]

            if uNode == vNode:
                return uNode

            # Lift both uNode and vNode simultaneously until their parents are the LCA
            for j in range(LOGN - 1, -1, -1):
                if up[uNode][j] != -1 and up[vNode][j] != -1 and up[uNode][j] != up[vNode][j]:
                    uNode = up[uNode][j]
                    vNode = up[vNode][j]

            # Parent of uNode is the LCA
            return up[uNode][0]

        # Process queries
        results = []
        for uQuery, vQuery in queries:
            # Path of length 0
            if uQuery == vQuery:
                results.append(0)
                continue

            lcaNode = getLCA(uQuery, vQuery)

            pathLen = depth[uQuery] + depth[vQuery] - (2 * depth[lcaNode])

            maxFreqOnPath = 0
            for w in range(1, (MAX_WEIGHT + 1)):
                # Count of weight w on path = (root to uQuery) + (root to vQuery) - 2 * (root to lcaNode)
                countWOnPath = pathCounts[uQuery][w] + pathCounts[vQuery][w] - (2 * pathCounts[lcaNode][w])
                if countWOnPath > maxFreqOnPath:
                    maxFreqOnPath = countWOnPath

            results.append(pathLen - maxFreqOnPath)

        return results