# Leetcode 2959: Number of Possible Sets of Closing Branches
# https://leetcode.com/problems/number-of-possible-sets-of-closing-branches/
# Solved on 1st of December, 2025
class Solution:
    def numberOfSets(self, n: int, maxDistance: int, roads: list[list[int]]) -> int:
        """
        Calculates the number of possible sets of closing branches such that the maximum distance
        between any two remaining branches is at most `maxDistance`.
        :param n: The number of branches.
        :param maxDistance: The maximum allowed distance between any two remaining branches.
        :param roads: A list of roads, where each road is [u, v, w] representing a road between branch u and branch v with weight w.
        :return: The number of valid sets of branches.
        """
        adj = [[float('inf')] * n for _ in range(n)]
        for i in range(n):
            adj[i][i] = 0
        for u, v, w in roads:
            adj[u][v] = min(adj[u][v], w)
            adj[v][u] = min(adj[v][u], w)

        numSets = 0
        for mask in range(1 << n):
            dist = [row[:] for row in adj]
            for k in range(n):
                if (mask >> k) & 1:
                    for i in range(n):
                        if (mask >> i) & 1:
                            for j in range(n):
                                if (mask >> j) & 1:
                                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

            isValid = True
            for i in range(n):
                if (mask >> i) & 1:
                    for j in range(n):
                        if (mask >> j) & 1:
                            if dist[i][j] > maxDistance:
                                isValid = False
                                break
                if not isValid:
                    break

            if isValid:
                numSets += 1

        return numSets