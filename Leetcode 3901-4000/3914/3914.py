# Leetcode 3914: Minimum Operations to Make Array Non Decreasing
# https://leetcode.com/problems/minimum-operations-to-make-array-non-decreasing/
# Solved on 10th of May, 2026
class Solution:
    def minOperations(self, nums: list[int]) -> int:
        """
        Calculates the minimum number of operations to make the array non-decreasing.

        :param nums: A list of integers to be modified.
        :return: The total number of operations required.
        """
        totalOperations = 0

        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                totalOperations += nums[i - 1] - nums[i]

        return totalOperations