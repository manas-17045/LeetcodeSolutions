# Leetcode 3600: Maximize Spanning Tree Stability with Upgrades
# https://leetcode.com/problems/maximize-spanning-tree-stability-with-upgrades/
# Solved on 6th of September, 2025
class Solution:
    def maxStability(self, n: int, edges: list[list[int]], k: int) -> int:
        """
        Maximizes the stability of a spanning tree by strategically using upgrades.

        Args:
            n (int): The number of nodes in the graph.
            edges (list[list[int]]): A list of edges, where each edge is [u, v, s, must].
                                     u, v are nodes, s is strength, and must (0 or 1) indicates if it's a must-use edge.
            k (int): The maximum number of upgrades allowed.

        Returns:
            int: The maximum possible stability. Returns -1 if no valid spanning tree can be formed.
        """
        class DSU:
            def __init__(self, size: int):
                self.parent = list(range(size))
                self.numComponents = size

            def find(self, i: int) -> int:
                if self.parent[i] == i:
                    return i
                self.parent[i] = self.find(self.parent[i])
                return self.parent[i]

            def union(self, i: int, j: int) -> bool:
                rootI = self.find(i)
                rootJ = self.find(j)
                if rootI != rootJ:
                    self.parent[rootI] = rootJ
                    self.numComponents -= 1
                    return True
                return False

        mustEdges = []
        optionalEdges = []
        for u, v, s, must in edges:
            if must == 1:
                mustEdges.append((u, v, s))
            else:
                optionalEdges.append((u, v, s))

        # Preliminary check for validity
        preCheckDsu = DSU(n)
        for u, v, s in mustEdges:
            if not preCheckDsu.union(u, v):
                return -1

        tempDsu = DSU(n)
        for edge in edges:
            tempDsu.union(edge[0], edge[1])
        if tempDsu.numComponents > 1:
            return -1

        def isPossible(minStrength: int) -> bool:
            dsu = DSU(n)
            upgradesUsed = 0

            for u, v, s in mustEdges:
                if s < minStrength:
                    return False
                dsu.union(u, v)

            for u, v, s in optionalEdges:
                if s >= minStrength:
                    dsu.union(u, v)

            for u, v, s in optionalEdges:
                if s < minStrength and 2 * s >= minStrength:
                    if dsu.find(u) != dsu.find(v):
                        if upgradesUsed < k:
                            upgradesUsed += 1
                            dsu.union(u, v)

            return dsu.numComponents == 1

        low = 0
        high = 200002
        ans = 0

        while low <= high:
            mid = low + (high - low) // 2
            if mid == 0:
                low = mid + 1
                continue

            if isPossible(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans