# Leetcode 2089: Find Target Indices After Sorting Array
# https://leetcode.com/problems/find-target-indices-after-sorting-array/
# Solved on 24th of May, 2025

class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        """
        Finds the indices of the target value in a sorted version of the input array.

        Args:
            nums: A list of integers.
            target: The integer value to find the indices of.

        Returns:
            A list of integers representing the indices of the target value in the sorted array.
        """
        nums.sort()
        # Create a list of tuples containing (value, original_index)
        indexed_nums = []
        for i, num in enumerate(nums):
            indexed_nums.append((num, i))

        # Sort the list based on the values (the first element of the tuple)
        indexed_nums.sort()

        # Find the original indices of the target value
        target_indices = []
        for num, original_index in indexed_nums:
            if num == target:
                target_indices.append(original_index)

        # The indices are already sorted because we iterated through the sorted list
        return target_indices