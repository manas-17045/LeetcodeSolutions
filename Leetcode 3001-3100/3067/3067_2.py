# Leetcode 3067: Count Pairs of Connectable Servers in a Weighted Tree Network
# https://leetcode.com/problems/count-pairs-of-connectable-servers-in-a-weighted-tree-network/
# Solved on 13th of August, 2025
class Solution:
    def countPairsOfConnectableServers(self, edges: list[list[int]], signalSpeed: int) -> list[int]:
        """
        Counts the number of pairs of connectable servers for each server in a tree structure.
        :param edges: A list of edges, where each edge is [u, v, w] representing a connection between server u and v with weight w.
        :param signalSpeed: The signal speed, used to determine connectable servers.
        :return: A list where ans[i] is the number of pairs of connectable servers if server i is the center.
        """
        n = len(edges) - 1
        g = [tuple() for _ in range(n)]
        for u, v, w in edges:
            g[u].append((v, w))
            g[v].append((u, w))

        # Count nodes in the subtree rooted at `u` (with parent `parent`)
        # whose distance from the center (root) is divisible by signalSpeed.
        def dfs(u: int, parent: int, dist_from_center: int) -> int:
            cnt = 1 if (dist_from_center % signalSpeed == 0) else 0
            for v, w in g[u]:
                if v == parent:
                    continue
                cnt += dfs(v, u, dist_from_center + w)
            return cnt

        ans = [0] * n
        for center in range(n):
            # Number of valid nodes counted in previously processed neighbor-subtrees
            pre = 0
            for v, w in g[center]:
                # Valid nodes in this neighbor-subtree
                cur = dfs(v, center, w)
                # Every node in this subtree can pair with any previously counted node
                ans[center] += cur * pre
                pre += cur
        return ans