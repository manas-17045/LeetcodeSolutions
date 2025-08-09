# Leetcode 2295: Replace Elements in an Array
# https://leetcode.com/problems/replace-elements-in-an-array/
# Solved on 9th of August, 2025
class Solution:
    def arrayChange(self, nums: list[int], operations: list[list[int]]) -> list[int]:
        """
        Applies a series of operations to an array, where each operation replaces an existing value with a new one.
        The function efficiently updates the array by maintaining a mapping of values to their indices.

        Args:
            nums (list[int]): The initial array of integers.
            operations (list[list[int]]): A list of operations, where each operation is [old_value, new_value].

        Returns:
            list[int]: The modified array after applying all operations.
        """
        # Map value -> index in nums
        pos = {val: i for i, val in enumerate(nums)}

        for old, new in operations:
            # Remove old value and get its index
            idx = pos.pop(old)
            # Update the array
            nums[idx] = new
            # Record new value's index
            pos[new] = idx

        return nums