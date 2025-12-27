# Leetcode 3708: Longest Fibonacci Subarray
# https://leetcode.com/problems/longest-fibonacci-subarray/
# Solved on 27th of December, 2025
class Solution:
    def longestSubarrays(self, nums: list[int]) -> int:
        """
        Finds the length of the longest Fibonacci-like subarray.

        Args:
            nums: A list of integers.
        Returns:
            The length of the longest Fibonacci-like subarray.
        """
        n = len(nums)

        maxLen = 0
        currentLen = 2
        for i in range(2, n):
            if nums[i] == nums[i - 1] + nums[i - 2]:
                currentLen += 1
            else:
                currentLen = 2

            if currentLen > maxLen:
                maxLen = currentLen

        return maxLen