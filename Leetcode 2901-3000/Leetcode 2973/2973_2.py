# Leetcode 2973: Find Number of Coins to Place in Tree Nodes
# https://leetcode.com/problems/find-number-of-coins-to-place-in-tree-nodes/
# Solved on 23rd of May, 2025

class Solution:
    def placedCoins(self, edges: list[list[int]], cost: list[int]) -> list[int]:
        """
        Calculates the number of coins to place in each tree node based on the costs of its descendants.

        For each node, we consider the costs of all nodes in its subtree.
        If the number of nodes in the subtree is less than 3, 1 coin is placed.
        Otherwise, we find the maximum product of three costs from the subtree.
        This maximum product can be either the product of the three largest positive costs
        or the product of the two smallest (most negative) costs and the largest positive cost.
        If the maximum product is negative or zero, 0 coins are placed.

        The solution uses a Depth First Search (DFS) to traverse the tree and collect the top 3 largest positive
        costs and the top 2 smallest negative costs from each subtree.
        """
        n = len(cost)
        # Build adjacency
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        ans = [0] * n

        def dfs(u: int, p: int):
            sz = 1
            # Start with u's own cost
            max_pos = [cost[u]] if cost[u] > 0 else []
            min_neg = [cost[u]] if cost[u] < 0 else []

            # Merge child info
            for v in g[u]:
                if v == p:
                    continue
                c_sz, c_max_pos, c_min_neg = dfs(v, u)
                sz += c_sz

                # Merge positive lists: keep only top 3
                if c_max_pos:
                    # Simple constant-size merge
                    tmp = max_pos + c_max_pos
                    # Partial sort for top 3
                    tmp.sort()
                    if len(tmp) > 3:
                        tmp = tmp[-3:]
                    max_pos = tmp

                # Merge negative lists: keep only bottom 3
                if c_min_neg:
                    tmp = min_neg + c_min_neg
                    tmp.sort()
                    if len(tmp) > 2:
                        tmp = tmp[:2]
                    min_neg = tmp

            # Now, compute ans[u]
            if sz < 3:
                # Too small, just 1 coin
                ans[u] = 1
            else:
                best = -10**30
                # Three largest positives
                if len(max_pos) >= 3:
                    best = max(best, max_pos[-1] * max_pos[-2] * max_pos[-3])
                # Two negatives × one largest positive
                if len(min_neg) >= 2 and len(max_pos) >= 1:
                    best = max(best, min_neg[0] * min_neg[1] * max_pos[-1])
                # Negative or zero => 0 coins
                ans[u] = best if best > 0 else 0

            return sz, max_pos, min_neg

        dfs(0, -1)
        return ans