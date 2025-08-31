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
            list[int]: A list where each element res[i] is the sum of |nums[i] - nums[j]| for all j.
        """
        n = len(nums)
        total = sum(nums)
        res = [0] * n
        left_sum = 0

        for i, v in enumerate(nums):
            # Sum of elements to the right of i
            right_sum = total - left_sum - v

            # Contribution from left elements: i * v - left_sum
            left_contrib = v * i - left_sum

            # Contribution from right elements: right_sum - (n - 1 - i) * v
            right_contrib = right_sum - (n - 1 - i) * v

            res[i] = left_contrib + right_contrib

            left_sum += v

        return res