# Leetcode 3638: Maximum Balanced Shipments
# https://leetcode.com/problems/maximum-balanced-shipments/
# Solved on 3rd of September, 2025
class Solution:
    def maxBalancedShipments(self, weight: list[int]) -> int:
        """
        Calculates the maximum number of balanced shipments.
        :param weight: A list of integers representing the weights of shipments.
        :return: An integer representing the maximum number of balanced shipments.
        """
        n = len(weight)
        count = 0
        cur_max = float('-inf')

        for w in weight:
            cur_max = max(cur_max, w)
            # Check balanced condition
            if w < cur_max:
                count += 1
                # Reset for next shipment
                cur_max = float('-inf')

        return count