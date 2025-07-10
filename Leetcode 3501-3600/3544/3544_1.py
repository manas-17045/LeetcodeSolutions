# Leetcode 3544: Subtree Inversion Sum
# https://leetcode.com/problems/subtree-inversion-sum/
# Solved on 10th of July, 2025
import sys


class Solution:
    def subtreeInversionSum(self, edges: list[list[int]], nums: list[int], k: int) -> int:
        """
        Calculates the maximum possible subtree inversion sum.

        Args:
            edges: A list of edges representing the tree.
            nums: A list of integers representing the values of nodes.
            k: The maximum distance for inversion propagation.

        Returns:
            The maximum subtree inversion sum.
        """
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return max(nums[0], -nums[0])

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        if (n + 50) > sys.getrecursionlimit():
            sys.setrecursionlimit(n + 50)

        memo = {}

        def dfs(u: int, p: int, parity: int, dist: int) -> int:
            state = (u, parity, dist)
            if state in memo:
                return memo[state]

            # Case 1: Do not invert node u
            childrenSumDontInvert = 0
            for v in adj[u]:
                if v != p:
                    newDist = min((dist + 1), k)
                    childrenSumDontInvert += dfs(v, u, parity, newDist)

            valDontInvert = nums[u] if parity == 0 else -nums[u]
            totalSumDontInvert = valDontInvert + childrenSumDontInvert

            # Case 2: Invert node u
            if dist < k:
                memo[state] = totalSumDontInvert
                return totalSumDontInvert

            childrenSumInvert = 0
            for v in adj[u]:
                if v != p:
                    childrenSumInvert += dfs(v, u, 1 - parity, 1)

            valInvert = -nums[u] if parity == 0 else nums[u]
            totalSumInvert = valInvert + childrenSumInvert

            result = max(totalSumDontInvert, totalSumInvert)
            memo[state] = result
            return result

        return dfs(0, -1, 0, k)