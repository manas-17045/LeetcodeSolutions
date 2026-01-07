# Leetcode 2789: Largest Element in an Array after Merge Operations
# https://leetcode.com/problems/largest-element-in-an-array-after-merge-operations/
# Solved on 7th of January, 2026
class Solution:
    def maxArrayValue(self, nums: list[int]) -> int:
        """
        Calculates the largest possible element in an array after performing merge operations.
        A merge operation can only be performed if the current element is less than or equal to the next element.

        :param nums: A list of integers.
        :return: The largest possible element after merge operations.
        """
        currentSum = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] <= currentSum:
                currentSum += nums[i]
            else:
                currentSum = nums[i]

        return currentSum