# Leetcode 3026: Maximum Good Subarray Sum
# https://leetcode.com/problems/maximum-good-subarray-sum/
# Solved on 31st of October, 2025
class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        """
        Calculates the maximum sum of a "good" subarray.
        A subarray is considered "good" if the absolute difference between its first and last elements is equal to k.

        Args:
            nums: A list of integers.
            k: An integer representing the required absolute difference between the first and last elements.
        Returns:
            The maximum sum of a good subarray. If no good subarray exists, returns 0.
        """
        n = len(nums)
        maxSum = -float('inf')
        foundGoodSubarray = False
        prefixSum = 0
        minPrefixForValue = {}

        for j in range(n):
            currentVal = nums[j]
            prefixBeforeJ = prefixSum
            prefixAfterJ = prefixSum + currentVal

            if currentVal not in minPrefixForValue:
                minPrefixForValue[currentVal] = prefixBeforeJ
            else:
                minPrefixForValue[currentVal] = min(minPrefixForValue[currentVal], prefixBeforeJ)

            startTarget1 = currentVal + k
            startTarget2 = currentVal - k

            if startTarget1 in minPrefixForValue:
                minStartPrefix = minPrefixForValue[startTarget1]
                subarraySum = prefixAfterJ - minStartPrefix
                maxSum = max(maxSum, subarraySum)
                foundGoodSubarray = True

            if startTarget2 in minPrefixForValue:
                minStartPrefix = minPrefixForValue[startTarget2]
                subarraySum = prefixAfterJ - minStartPrefix
                maxSum = max(maxSum, subarraySum)
                foundGoodSubarray = True

            prefixSum = prefixAfterJ

        return int(maxSum) if foundGoodSubarray else 0