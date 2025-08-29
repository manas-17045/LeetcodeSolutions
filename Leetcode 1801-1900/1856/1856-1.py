# Leetcode 1856: Maximum Subarray Min-Product
# https://leetcode.com/problems/maximum-subarray-min-product/
# Solved on 29th of August, 2025
class Solution:
    def maxSumMinProduct(self, nums: list[int]) -> int:
        """
        Calculates the maximum subarray min-product. The min-product of an array is defined as
        the minimum value in the array multiplied by the sum of all elements in the array.

        Args:
            nums: A list of integers.
        Returns:
            The maximum subarray min-product modulo 10^9 + 7.
        """
        n = len(nums)
        MOD = 10**9 + 7

        prefixSum = [0] * (n + 1)
        for i in range(n):
            prefixSum[i + 1] = prefixSum[i] + nums[i]

        leftBound = [-1] * n
        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            if stack:
                leftBound[i] = stack[-1]
            stack.append(i)

        rightBound = [n] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] > nums[i]:
                stack.pop()
            if stack:
                rightBound[i] = stack[-1]
            stack.append(i)

        maxProduct = 0
        for i in range(n):
            leftIndex = leftBound[i]
            rightIndex = rightBound[i]

            subarraySum = prefixSum[rightIndex] - prefixSum[leftIndex + 1]

            currentProduct = nums[i] * subarraySum
            if currentProduct > maxProduct:
                maxProduct = currentProduct

        return maxProduct % MOD