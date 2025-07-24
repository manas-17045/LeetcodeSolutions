# Leetcode 2322: Minimum Score After Removals on a Tree
# https://leetcode.com/problems/minimum-score-after-removals-on-a-tree/
# Solved on 24th of July, 2025
import sys
sys.setrecursionlimit(10**7)


class Solution:
    def minimumScore(self, nums: list[int], edges: list[list[int]]) -> int:
        """
        Calculates the minimum score achievable by removing two edges from a tree.

        Args:
            nums: A list of integers representing the values of the nodes.
            edges: A list of lists representing the edges of the tree.
        """

        n = len(nums)
        # build adjacency
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        # parent, subtree xor, tin/tout for ancestor checks
        parent = [-1] * n
        subXor = [0] * n
        tin = [0] * n
        tout = [0] * n
        timer = 0

        def dfs(u: int, p: int):
            nonlocal timer
            parent[u] = p
            subXor[u] = nums[u]
            tin[u] = timer
            timer += 1
            for v in g[u]:
                if v == p:
                    continue
                dfs(v, u)
                subXor[u] ^= subXor[v]
            tout[u] = timer

        dfs(0, -1)
        total_xor = subXor[0]

        # Orient edges: Pick the deeper node as the "subtree" being cut off
        cuts = []
        for u, v in edges:
            if parent[v] == u:
                cuts.append(v)
            elif parent[u] == v:
                cuts.append(u)
            else:
                # shouldn't happen in a tree once rooted
                # but if it does, just pick either
                cuts.append(v)

        def is_ancestor(a: int, b: int) -> bool:
            # u is ancestor of v if tin[u] <= tin[v] < tout[u]
            return tin[a] <= tin[b] < tout[a]

        best = float('inf')
        m = len(cuts)
        for i in range(m):
            a = cuts[i]
            for j in range(i + 1, m):
                b = cuts[j]
                # three components' XORs
                if is_ancestor(a, b):
                    # b-subtree inside a-subtree
                    x1 = subXor[b]
                    x2 = subXor[a] ^ subXor[b]
                    x3 = total_xor ^ subXor[a]
                elif is_ancestor(b, a):
                    # a-subtree inside b-subtree
                    x1 = subXor[a]
                    x2 = subXor[b] ^ subXor[a]
                    x3 = total_xor ^ subXor[b]
                else:
                    # disjoint
                    x1 = subXor[a]
                    x2 = subXor[b]
                    x3 = total_xor ^ x1 ^ x2
                cur = max(x1, x2, x3) - min(x1, x2, x3)
                if cur < best:
                    best = cur

        return best