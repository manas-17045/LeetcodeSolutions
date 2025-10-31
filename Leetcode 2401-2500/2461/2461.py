# Leetcode 2461: Maximum Sum of Distinct Subarrays With Length K
# https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/
# Solved on 31st of October, 2025
class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        """
        Calculates the maximum sum of a subarray of length k with distinct elements.

        Args:
            nums: A list of integers.
            k: The desired length of the subarray.
        Returns:
            The maximum sum of a subarray of length k with distinct elements.
        """

        maxSum = 0
        currentSum = 0
        windowCounts = {}
        left = 0

        for right in range(len(nums)):
            currentNum = nums[right]
            currentSum += currentNum
            windowCounts[currentNum] = windowCounts.get(currentNum, 0) + 1

            windowSize = right - left + 1

            if windowSize == k:
                if len(windowCounts) == k:
                    maxSum = max(maxSum, currentSum)

                leftNum = nums[left]
                currentSum -= leftNum
                windowCounts[leftNum] -= 1

                if windowCounts[leftNum] == 0:
                    del windowCounts[leftNum]

                left += 1

        return maxSum