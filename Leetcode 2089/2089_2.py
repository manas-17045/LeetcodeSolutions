# Leetcode 2089: Find Target Indices After Sorting Array
# https://leetcode.com/problems/find-target-indices-after-sorting-array/
# Solved on 24th of May, 2025

class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        """
        Finds the indices of all occurrences of the target value in a sorted version of the input array.

        Args:
            nums: A list of integers.
            target: The integer value to find the indices of.

        Returns:
            A list of integers representing the indices of the target value in the sorted array.
        """
        nums.sort()
        less = 0
        equal = 0
        for v in nums:
            if v < target:
                less += 1
            elif v == target:
                equal += 1

        # If there are no occurrences of target, return empty list
        if equal == 0:
            return []

        # Build the list of indices [less, less+1, ..., less+equal-1]
        return list(range(less, less + equal))