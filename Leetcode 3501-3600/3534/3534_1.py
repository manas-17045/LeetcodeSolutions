# Leetcode 3534: Path Existence Queries in a Graph II
# https://leetcode.com/problems/path-existence-queries-in-a-graph-ii/
# Solved on 8th of June, 2025
import sys
sys.setrecursionlimit(2 * 10**5)

class DSU:
    def __init(self, n: int):
        self.parent = list(range(n))

    def find(self, i: int) -> int:
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i: int, j: int) -> None:
        rootI = self.find(i)
        rootJ = self.find(j)
        if rootI != rootJ:
            self.parent[rootI] = rootJ

class Solution:
    def pathExistenceQueries(self, n: int, nums: list[int], maxDiff: int, queries: list[list[int]]) -> list[int]:
        """
        Given a graph where nodes are indexed from 0 to n-1, and each node i has a value nums[i].
        An edge exists between nodes i and j if abs(nums[i] - nums[j]) <= maxDiff.
        We are given a list of queries [u, v], and for each query, we need to find the minimum
        number of edges in a path from u to v. If no path exists, return -1.

        Args:
            n: The number of nodes in the graph.
            nums: A list of integers representing the values of the nodes.
            maxDiff: The maximum allowed absolute difference between values of connected nodes.
            queries: A list of queries, where each query is a list [u, v].

        Returns:
            A list of integers, where the i-th element is the minimum number of edges in a path
            from queries[i][0] to queries[i][1], or -1 if no path exists.
        """
        sortedNodes = sorted([(nums[i], i) for i in range(n)])

        dsu = DSU(n)
        if n > 1:
            for i in range(n - 1):
                if sortedNodes[i + 1][0] - sortedNodes[i][0] <= maxDiff:
                    dsu.union(sortedNodes[i][1], sortedNodes[i + 1][1])

        pos = {originalIndex: i for i, (num, originalIndex) in enumerate(sortedNodes)}

        maxLog = n.bit_length()

        lReach = [[0] * n for _ in range(maxLog)]
        rReach = [[0] * n for _ in range(maxLog)]

        l, r = 0, 0
        for i in range(n):
            while sortedNodes[i][0] - sortedNodes[l][0] > maxDiff:
                l += 1
            while r < n and sortedNodes[r][0] - sortedNodes[i][0] <= maxDiff:
                r += 1
            lReach[0][i] = l
            rReach[0][i] = r - 1

        for k in range(1, maxLog):
            for i in range(n):
                lReach[k][i] = lReach[k - 1][lReach[k - 1][i]]
                rReach[k][i] = rReach[k - 1][rReach[k - 1][i]]

        results = []
        for u, v in queries:
            if dsu.find(u) != dsu.find(v):
                results.append(-1)
                continue

            uPos, vPos = pos[u], pos[v]

            if uPos == vPos:
                results.append(0)
                continue

            ans = 0
            currL, currR = uPos, uPos

            for k in range(maxLog - 1, -1, -1):
                nextL = lReach[k][currL]
                nextR = rReach[k][currR]

                if not (nextL <= vPos <= nextR):
                    ans += (1 << k)
                    currL = nextL
                    currR = nextR

            results.append(ans + 1)

        return results