# Leetcode 3810: Minimum Operations to Reach Target Array
# https://leetcode.com/problems/minimum-operations-to-reach-target-array/
# Solved on 23rd of January, 2026
class Solution:
    def minOperations(self, nums: list[int], target: list[int]) -> int:
        """
        Calculates the minimum number of operations to reach the target array.

        Args:
            nums (list[int]): The initial array of integers.
            target (list[int]): The target array of integers.

        Returns:
            int: The number of unique values in nums that need to be changed.
        """
        valuesToChange = set()

        for num, finalValue in zip(nums, target):
            if num != finalValue:
                valuesToChange.add(num)

        return len(valuesToChange)