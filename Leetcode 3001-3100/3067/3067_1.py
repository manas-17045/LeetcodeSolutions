# Leetcode 3067: Count Pairs of Connectable Servers in a Weighted Tree Network
# https://leetcode.com/problems/count-pairs-of-connectable-servers-in-a-weighted-tree-network/
# Solved on 13th of August, 2025
class Solution:
    def countPairsOfConnectableServers(self, edges: list[list[int]], signalSpeed: int) -> list[int]:
        """
        Counts the number of pairs of connectable servers for each server in a weighted tree network.

        Args:
            edges: A list of edges, where each edge is [u, v, w] representing a connection between server u and v with weight w.
            signalSpeed: The speed at which signals travel.
        """
        n = len(edges) + 1
        adj = [tuple() for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))

        def dfs(u, p, dist):
            count = 1 if dist % signalSpeed == 0 else 0
            for v, w in adj[u]:
                if v != p:
                    count += dfs(v, u, dist + w)
            return count

        ans = [0] * n
        for i in range(n):
            if len(adj[i]) < 2:
                continue

            runningSum = 0
            totalPairs = 0
            for neighbor, weight in adj[i]:
                countInBranch = dfs(neighbor, i, weight)
                totalPairs += countInBranch * runningSum
                runningSum += countInBranch

            ans[i] = totalPairs

        return ans