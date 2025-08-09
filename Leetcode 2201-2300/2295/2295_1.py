# Leetcode 2295: Replace Elements in an Array
# https://leetcode.com/problems/replace-elements-in-an-array/
# Solved on 9th of August, 2025
class Solution:
    def arrayChange(self, nums: list[int], operations: list[list[int]]) -> list[int]:
        """
        Replaces elements in the `nums` array based on the given `operations`.

        Args:
            nums (list[int]): The initial array of integers.
            operations (list[list[int]]): A list of operations, where each operation is [oldValue, newValue].
        Returns:
            list[int]: The modified array after applying all operations.
        """
        valToIndexMap = {val: i for i, val in enumerate(nums)}

        for oldVal, newVal in operations:
            index = valToIndexMap[oldVal]
            nums[index] = newVal

            valToIndexMap[newVal] = index
            del valToIndexMap[oldVal]

        return nums