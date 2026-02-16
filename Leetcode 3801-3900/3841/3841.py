# Leetcode 3841: Palindromic Path Queries in a Tree
# https://leetcode.com/problems/palindromic-path-queries-in-a-tree/
# Solved on 16th of February, 2026
import sys
sys.setrecursionlimit(100000)


class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        """
        Determines if the path between two nodes in a tree can form a palindrome after reordering,
        while supporting point updates on node characters.

        :param n: Number of nodes in the tree.
        :param edges: List of undirected edges representing the tree structure.
        :param s: Initial string where s[i] is the character assigned to node i.
        :param queries: List of query strings ("update u c" or "query u v").
        :return: A list of booleans representing the results of the path queries.
        """
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        tin = [0] * n
        tout = [0] * n
        depth = [0] * n
        up = [[0] * 17 for _ in range(n)]
        timer = 0

        def dfs(u, p, d):
            nonlocal timer
            timer += 1
            tin[u] = timer
            depth[u] = d

            up[u][0] = p
            for i in range(1, 17):
                up[u][i] = up[up[u][i - 1]][i - 1]

            for v in adj[u]:
                if v != p:
                    dfs(v, u, d + 1)

            tout[u] = timer

        dfs(0, 0, 0)

        def getLca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            diff = depth[u] - depth[v]
            for i in range(17):
                if (diff >> i) & 1:
                    u = up[u][i]

            if u == v:
                return u

            for i in range(16, -1, -1):
                if up[u][i] != up[v][i]:
                    u = up[u][i]
                    v = up[v][i]

            return up[u][0]

        bit = [0] * (n + 2)

        def updateBit(idx, val):
            while idx <= n + 1:
                bit[idx] ^= val
                idx += idx & (-idx)

        def queryBit(idx):
            res = 0
            while idx > 0:
                res ^= bit[idx]
                idx -= idx & (-idx)
            return res

        def rangeUpdate(l, r, val):
            updateBit(l, val)
            updateBit(r + 1, val)

        chars = [1 << (ord(c) - 97) for c in s]
        for i in range(n):
            rangeUpdate(tin[i], tout[i], chars[i])

        ans = []
        for q in queries:
            parts = q.split()
            if parts[0] == 'update':
                u = int(parts[1])
                charVal = 1 << (ord(parts[2]) - 97)
                diff = chars[u] ^ charVal

                if diff:
                    chars[u] = charVal
                    rangeUpdate(tin[u], tout[u], diff)
            else:
                u = int(parts[1])
                v = int(parts[2])
                lca = getLca(u, v)

                pathMask = queryBit(tin[u]) ^ queryBit(tin[v]) ^ chars[lca]

                if pathMask & (pathMask - 1) == 0:
                    ans.append(True)
                else:
                    ans.append(False)

        return ans