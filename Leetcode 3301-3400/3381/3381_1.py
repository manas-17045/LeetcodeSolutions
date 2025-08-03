# Leetcode 3381: Maximum Subarray Sum With Length Divisible by K
# https://leetcode.com/problems/maximum-subarray-sum-with-length-divisible-by-k/
# Solved on 3rd of August, 2025
import math


class Solution:
    def maxSubarraySum(self, nums: list[int], k: int) -> int:
        """
        Calculates the maximum subarray sum where the length of the subarray is divisible by k.

        Args:
            nums (list[int]): The input list of integers.
            k (int): The divisor for the subarray length.
        Returns:
            int: The maximum subarray sum with length divisible by k.
        """
        minPrefixSum = [math.inf] * k
        minPrefixSum[0] = 0

        maxSum = -math.inf
        currentSum = 0

        for i in range(len(nums)):
            currentSum += nums[i]
            remainder = (i + 1) % k

            if minPrefixSum[remainder] != math.inf:
                maxSum = max(maxSum, currentSum - minPrefixSum[remainder])

            minPrefixSum[remainder] = min(minPrefixSum[remainder], currentSum)

        return maxSum