# Leetcode 1685: Sum of Absolute Differences in a Sorted Array
# https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array/
# Solved on 31st of August, 2025
class Solution:
    def getSumAbsoluteDifferences(self, nums: list[int]) -> list[int]:
        """
        Calculates the sum of absolute differences for each element in a sorted array.

        Args:
            nums (list[int]): A list of integers sorted in non-decreasing order.
        Returns:
            list[int]: A list where each element result[i] is the sum of |nums[i] - nums[j]| for all j.
        """
        n = len(nums)
        totalSum = sum(nums)
        leftSum = 0
        result = []

        for i, num in enumerate(nums):
            currentResult = (2 * i - n) * num + totalSum - (2 * leftSum)
            result.append(currentResult)
            leftSum += num

        return result