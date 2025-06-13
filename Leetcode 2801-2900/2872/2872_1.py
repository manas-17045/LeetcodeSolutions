# Leetcode 2872: Maximum Number of K-Divisible Components
# https://leetcode.com/problems/maximum-number-of-k-divisible-components/
# Solved on 21st of December, 2024

class Solution:
    def dfs(self, graph: list[list[int]], u: int, prev: int, values: list[int], k: int) -> int:
        tree_sum = values[u]

        for v in graph[u]:
            if v != prev:
                tree_sum += self.dfs(graph, v, u, values, k)

        if tree_sum % k == 0:
            self.ans += 1

        return tree_sum

    # Main Function
    def maxKDivisibleComponents(self, n: int, edges: list[list[int]], values: list[int], k: int) -> int:
        """
        Given a tree with n nodes where each node has a value, and an integer k,
        we need to find the maximum number of k-divisible components we can obtain
        by removing some edges. A k-divisible component is a connected component
        where the sum of its node values is divisible by k.

        Args:
            n: The number of nodes in the tree.
            edges: A list of edges representing the tree.
            values: A list of values for each node.
            k: The integer to check for divisibility.
        """
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        self.ans = 0
        self.dfs(graph, 0, -1, values, k)
        return self.ans