# Leetcode 2068: Find the Maximum Sum of Node Values
# https://leetcode.com/problems/find-the-maximum-sum-of-node-values/
# Solved on 23rd of May, 2025

class Solution:
    def maximumValueSum(self, nums: list[int], k: int, edges: list[list[int]]) -> int:
        """
        Finds the maximum possible sum of node values after applying the XOR operation
        (with k) to any pair of connected nodes any number of times.

        The key insight is that XORing two connected nodes with k is equivalent to
        XORing each of those two nodes individually with k. This can be repeated,
        meaning we can effectively choose to XOR any subset of nodes with k, as long
        as the number of chosen nodes is even.

        Args:
            nums: A list of integers representing the values of the nodes.
            k: An integer to XOR with.
            edges: A list of lists representing the edges of the tree (not directly used in the logic).
        """
        initial_total_sum = 0
        for x in nums:
            initial_total_sum += x

        # This will store the sum of deltas if we pick all nodes that have a positive delta.
        sum_of_all_positive_deltas = 0
        # This counts how many nodes provide a positive delta.
        count_of_nodes_with_positive_delta = 0

        # To handle the odd count case, we need:
        # The smallest positive delta encountered 9to subtract if we un-pick a positive delta node).
        min_positive_delta_value = float('inf')
        # The largest non-positive delta encountered (to add if we pick an additional non-positive delta node).
        max_negative_delta_value = float('-inf')

        for num_val in nums:
            delta = (num_val ^ k) - num_val

            if delta > 0:
                sum_of_all_positive_deltas += delta
                count_of_nodes_with_positive_delta += 1
                min_positive_delta_value = min(min_positive_delta_value, delta)
            else:   # delta <= 0
                max_negative_delta_value = max(max_negative_delta_value, delta)

        # This will be the final net profit from operations.
        final_max_profit_from_deltas = 0

        if count_of_nodes_with_positive_delta % 2 == 0:
            # If the number of nodes that give a positive delta is even,
            # we can choose all of them. This is optimal.
            final_max_profit_from_deltas = sum_of_all_positive_deltas
        else:
            # The number of nodes that give a positive delta is odd.
            # We must make the count of chosen nodes (those whose values are effectively XORed) even.

            # Option 1: Do not choose one of the positive-delta nodes.
            # To maximize profit, we un-select the one with the smallest positive delta.
            # This is always possible because count_of_nodes_with_positive_delta is odd, so it's >= 1,
            # meaning min_positive_delta_value is a valid number.
            profit_if_sacrificing_smallest_positive = sum_of_all_positive_deltas - min_positive_delta_value

            # Option 2: Choose one additional node that has a non-positive delta.
            # To maximize profit, we select the one with the largest non-positive delta (value closest to 0).
            # This is only possible if at least one non-positive delta exists.
            if max_negative_delta_value > float('-inf'):    # Check if max_negative_delta_value was updated (i.e,
                # atleast one non-positive delta exists)
                profit_if_including_largest_negative = sum_of_all_positive_deltas + max_negative_delta_value
                final_max_profit_from_deltas = max(profit_if_sacrificing_smallest_positive, profit_if_including_largest_negative)
            else:
                # No non-positive deltas exist (all deltas were positive)
                # We must choose Option1 (sacrificing the smallest positive delta).
                final_max_profit_from_deltas = profit_if_sacrificing_smallest_positive

        return initial_total_sum + final_max_profit_from_deltas