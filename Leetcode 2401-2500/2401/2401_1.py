# Leetcode 2401: Longest Nice Subarray
# https://leetcode.com/problems/longest-nice-subarray/
# Solved on 31st of July, 2025
class Solution:
    def longestNiceSubarray(self, nums: list[int]) -> int:
        """
        Finds the length of the longest "nice" subarray.
        A subarray is considered "nice" if the bitwise AND of any two distinct elements in the subarray is 0.

        Args:
            nums (list[int]): The input list of integers.
        Returns:
            int: The length of the longest nice subarray.
        """
        maxLen = 0
        currentOr = 0
        leftIndex = 0
        
        for rightIndex in range(len(nums)):
            while (currentOr & nums[rightIndex]) != 0:
                currentOr ^= nums[leftIndex]
                leftIndex += 1
            
            currentOr |= nums[rightIndex]
            maxLen = max(maxLen, rightIndex - leftIndex + 1)
            
        return maxLen