# Leetcode 1827: Minimum Operations to Make the Array Increasing
# https://leetcode.com/problems/minimum-operations-to-make-the-array-increasing/
# Solved on 5th of December, 2025
class Solution:
    def minOperations(self, nums: list[int]) -> int:
        """
        Calculates the minimum number of operations required to make the array strictly increasing.

        Args:
            nums (list[int]): The input list of integers.
        Returns:
            int: The minimum number of operations.
        """
        totalOperations = 0

        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                difference = nums[i - 1] - nums[i] + 1
                totalOperations += difference
                nums[i] += difference

        return totalOperations