# Leetcode 3544: Subtree Inversion Sum
# https://leetcode.com/problems/subtree-inversion-sum/
# Solved on 10th of July, 2025
import sys


class Solution:
    def subtreeInversionSum(self, edges: list[list[int]], nums: list[int], k: int) -> int:
        """
        Calculates the maximum possible sum of node values in a subtree, considering inversions.

        Args:
            edges: A list of lists representing the edges of the tree.
            nums: A list of integers where nums[i] is the value of node i.
            k: An integer representing the maximum allowed depth for a path.

        Returns:
            The maximum possible sum of node values in a subtree.
        """
        sys.setrecursionlimit(10**7)
        n = len(nums)

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(u: int, parent: int) -> list[list[int]]:
            child_dp = []
            for v in adj[u]:
                if v == parent:
                    continue
                child_dp.append(dfs(v, u))

            sum_children = [[0, 0] for _ in range(k + 1)]
            for dp_c in child_dp:
                for d in range(1, (k + 1)):
                    sum_children[d][0] += dp_c[d][0]
                    sum_children[d][1] += dp_c[d][1]

            dp_u = [[-10**30, -10**30] for _ in range(k + 1)]
            for d_p in range(1, (k + 1)):
                for p_p in (0, 1):
                    nd = d_p + 1 if d_p < k else k
                    base = nums[u] if p_p == 0 else -nums[u]
                    best = base + sum_children[nd][p_p]

                    if d_p == k:
                        p2 = p_p ^ 1
                        base2 = nums[u] if p2 == 0 else -nums[u]
                        cand = base2 + sum_children[1][p2]
                        if cand > best:
                            best = cand

                    dp_u[d_p][p_p] = best

            return dp_u

        root_dp = dfs(0, -1)
        return root_dp[k][0]