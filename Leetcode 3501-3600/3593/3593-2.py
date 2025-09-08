# Leetcode 3593: Minimum Increments to Equalize Leaf Paths
# https://leetcode.com/problems/minimum-increments-to-equalize-leaf-paths/
# Solved on 7th of September, 2025
from collections import defaultdict


class Solution:
    def minIncrease(self, n: int, edges: list[list[int]], cost: list[int]) -> int:
        """
        Calculates the minimum number of increases required to make the sum of costs from any node to a leaf
        equal for all paths starting from a given node.

        Args:
            n (int): The number of nodes in the tree.
            edges (list[list[int]]): A list of edges representing the tree.
            cost (list[int]): A list where cost[i] is the cost of node i.

        Returns:
            int: The minimum number of increases needed.
        """
        # Build adjacency list
        tree = defaultdict(list)
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)

        def dfs(node: int, parent: int) -> (int, int):
            # Leaf node
            if len(tree[node]) == 1 and parent != 1:
                return cost[node], 0

            max_child_sum = 0
            total_changes = 0
            child_sums = []

            for child in tree[node]:
                if child == parent:
                    continue

                child_sum, child_changes = dfs(child, node)
                total_changes += child_changes
                child_sums.append(child_sum)
                max_child_sum = max(max_child_sum, child_sum)

            # Equalize all children to max_child_sum
            for s in child_sums:
                if s < max_child_sum:
                    total_changes += 1

            return cost[node] + max_child_sum, total_changes

        _, changes = dfs(0, -1)
        return changes