# Leetcode 3107: Minimum Operations to Make Median of Array Equal to K
# https://leetcode.com/problems/minimum-operations-to-make-median-of-array-equal-to-k/
# Solved on 18th of October, 2025
class Solution:
    def minOperationsToMakeMedianK(self, nums: list[int], k: int) -> int:
        """
        Calculates the minimum number of operations to make the median of the array equal to k.

        Args:
            nums: A list of integers.
            k: The target value for the median.

        Returns:
            The minimum number of operations.
        """

        nums.sort()
        n = len(nums)
        medianIndex = n // 2

        totalOperations = 0

        for i in range(medianIndex):
            if nums[i] > k:
                totalOperations += nums[i] - k

        totalOperations += abs(nums[medianIndex] - k)

        for i in range(medianIndex + 1, n):
            if nums[i] < k:
                totalOperations += k - nums[i]

        return totalOperations