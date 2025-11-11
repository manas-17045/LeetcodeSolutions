# Leetcode 3427: Sum of Variable Length Subarrays
# https://leetcode.com/problems/sum-of-variable-length-subarrays/
# Solved on 11th of November, 2025
class Solution:
    def subarraySum(self, nums: list[int]) -> int:
        """
        Calculates the sum of variable length subarrays based on the problem description.

        Args:
            nums: A list of integers.
        Returns:
            The total sum of the variable length subarrays.
        """
        n = len(nums)
        prefixSum = [0] * (n + 1)

        for i in range(n):
            prefixSum[i + 1] = prefixSum[i] + nums[i]

        totalSum = 0
        for i in range(n):
            start = max(0, (i - nums[i]))
            currentSubarraySum = prefixSum[i + 1] - prefixSum[start]
            totalSum += currentSubarraySum

        return totalSum