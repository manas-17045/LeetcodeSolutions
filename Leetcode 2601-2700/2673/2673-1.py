# Leetcode 2673: Make Costs of Paths Equal in a Binary Tree
# https://leetcode.com/problems/make-costs-of-paths-equal-in-a-binary-tree/
# Solved on 8th of October, 2025
class Solution:
    def minIncrements(self, n: int, cost: list[int]) -> int:
        """
        Calculates the minimum increments needed to make the costs of all paths from the root to a leaf equal.

        Args:
            n (int): The number of nodes in the binary tree.
            cost (list[int]): A 0-indexed array where cost[i] is the cost of the (i+1)th node.

        Returns:
            int: The minimum total increments needed.
        """
        # The total number of increments needed
        totalIncrements = 0

        # Iterate over all internal nodes from the lowest level up to the root (node 1)
        for i in range(n // 2, 0, -1):
            leftChildIndex = 2 * i
            rightChildIndex = 2 * i + 1

            pathSumLeft = cost[leftChildIndex - 1]
            pathSumRight = cost[rightChildIndex - 1]

            # The difference is the number of increments needed to equalize the subtrees
            incrementNeeded = abs(pathSumLeft - pathSumRight)
            totalIncrements += incrementNeeded

            maxPathSum = max(pathSumLeft, pathSumRight)
            cost[i - 1] += maxPathSum

        return totalIncrements