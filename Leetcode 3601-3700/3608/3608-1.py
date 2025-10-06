# Leetcode 3608: Minimum Time for K Connected Components
# https://leetcode.com/problems/minimum-time-for-k-connected-components/
# Solved on 6th of October, 2025
class DSU:
    def __init__(self, count):
        self.parent = list(range(count))
        self.nodeSize = [1] * count
        self.componentCount = count

    def find(self, index):
        if self.parent[index] == index:
            return index
        self.parent[index] = self.find(self.parent[index])
        return self.parent[index]

    def union(self, indexOne, indexTwo):
        rootOne = self.find(indexOne)
        rootTwo = self.find(indexTwo)
        if rootOne != rootTwo:
            if self.nodeSize[rootOne] < self.nodeSize[rootTwo]:
                rootOne, rootTwo = rootTwo, rootOne
            self.parent[rootTwo] = rootOne
            self.nodeSize[rootOne] += self.nodeSize[rootTwo]
            self.componentCount -= 1

class Solution:
    def minTime(self, n: int, edges: list[list[int]], k: int) -> int:
        """
        Calculates the minimum time `T` such that if we only consider edges with time `t <= T`,
        the graph has at least `k` connected components.

        Args:
            n: The number of nodes in the graph.
            edges: A list of edges, where each edge is `[u, v, t]` representing a connection between node `u` and `v` with time `t`.
            k: The target number of connected components.

        Returns:
            The minimum time `T` that satisfies the condition.
        """
        def check(timeLimit):
            dsu = DSU(n)
            for u, v, t in edges:
                if t > timeLimit:
                    dsu.union(u, v)
            return dsu.componentCount >= k

        searchLow = 0
        searchHigh = 1000000001
        minTimeResult = searchHigh

        while searchLow <= searchHigh:
            searchMid = searchLow + (searchHigh - searchLow) // 2

            if check(searchMid):
                minTimeResult = searchMid
                searchHigh = searchMid - 1
            else:
                searchLow = searchMid + 1

        return minTimeResult