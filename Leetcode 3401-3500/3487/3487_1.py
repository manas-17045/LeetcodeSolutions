# Leetcode 3487: Maximum Unique Subarray Sum After Deletion
# https://leetcode.com/problems/maximum-unique-subarray-sum-after-deletion/
# Solved on 25th of July, 2025
class Solution:
    def maxSum(self, nums: list[int]) -> int:
        """
        This function calculates the maximum unique subarray sum after deletion.

        Args:
            nums (list[int]): The input list of integers.
        Returns:
            int: The maximum unique subarray sum.
        """
        uniqueElements = set(nums)

        sumOfNonNegatives = 0
        hasNonNegative = False

        for num in uniqueElements:
            if num >= 0:
                sumOfNonNegatives += num
                hasNonNegative = True

        if not hasNonNegative:
            return sumOfNonNegatives
        else:
            return max(uniqueElements)