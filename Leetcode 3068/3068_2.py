# Leetcode 2068: Find the Maximum Sum of Node Values
# https://leetcode.com/problems/find-the-maximum-sum-of-node-values/
# Solved on 23rd of May, 2025

class Solution:
    def maximumValueSum(self, nums: list[int], k: int, edges: list[list[int]]) -> int:
        """
        Finds the maximum possible sum of node values after performing XOR operations.

        Args:
            nums: A list of integers representing the initial values of the nodes.
            k: An integer representing the value to XOR with.
            edges: A list of lists representing the edges of the tree (irrelevant for the solution).

        Returns:
            The maximum possible sum of node values.
        """
        # Edges form a connected tree but are otherwise irrelevant,
        # since any even-sized subset of nodes can be flipped.
        total = 0
        cnt_pos = 0
        min_abs_gain = float('inf')

        for x in nums:
            y = x ^ k
            gain = y - x
            # If flipping this node increases the sum, take it
            if gain > 0:
                total += y
                cnt_pos += 1
            else:
                total += x
            # Track the smallest |gain| for parity-fixing
            min_abs_gain = min(min_abs_gain, abs(gain))

        # If we flipped an odd number of nodes, undo the smallest-gain flip
        if cnt_pos % 2 == 1:
            total -= min_abs_gain

        return total