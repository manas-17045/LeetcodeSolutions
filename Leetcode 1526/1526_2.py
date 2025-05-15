# Leetcode 1526: Minimum Number of Increments on Subarrays to Form a Target Array
# https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array/
# Solved on 15th of May, 2025

class Solution:
    def minNumberOperations(self, target: list[int]) -> int:
        """
        Given an array of integer target, you want to build an array of the same length initialized with zeros.
        In one operation, you can select any subarray and increment each element by one.
        Return the minimum number of operations needed to achieve the target array.

        Args:
            target (list[int]): The target array of integers.
        Returns:
            int: The minimum number of operations needed. """
        # You need target[0] operations to build up from 0 to target[0].
        # Afterwards, whenever target[i] > target[i - 1], you need
        # (target[i] - target[i - 1]) more operations for that increase.
        ops = target[0]
        for i in range(1, len(target)):
            diff = target[i] - target[i - 1]
            if diff > 0:
                ops += diff
        return ops