# Leetcode 2673: Make Costs of Paths Equal in a Binary Tree
# https://leetcode.com/problems/make-costs-of-paths-equal-in-a-binary-tree/
# Solved on 8th of October, 2025
class Solution:
    def minIncrements(self, n: int, cost: list[int]) -> int:
        """
        Calculates the minimum increments needed to make all paths from the root to any leaf in a binary tree have the same total cost.
        :param n: The number of nodes in the binary tree.
        :param cost: A list of integers where cost[i] is the cost of the (i+1)-th node.
        :return: The total minimum increments required.
        """
        self.total_increments = 0

        def dfs(node_idx):
            left_child = 2 * node_idx
            right_child = 2 * node_idx + 1

            # If left child index exceeds n, this is a leaf.
            if left_child > n:
                return cost[node_idx - 1]

            # Recursively get max path costs from left and right subtrees
            left_max = dfs(left_child)
            right_max = dfs(right_child)

            # We need to make both paths equal by incrementing the smaller one
            self.total_increments += abs(left_max - right_max)

            # Return the max path cost from current node downward
            return cost[node_idx - 1] + max(left_max, right_max)

        dfs(1)
        return self.total_increments