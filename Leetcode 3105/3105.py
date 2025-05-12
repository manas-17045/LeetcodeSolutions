# Leetcode 3105: Longest Strictly Increasing or Strictly Decreasing Subarray
# https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/

class Solution:
    def longestMonotonicSubarray(self, nums: list[int]) -> int:
        """
        Finds the length of the longest strictly increasing or strictly decreasing subarray within a given array of integers.

        Args:
            nums: A list of integers.

        Returns:
            The length of the longest monotonic subarray.  Returns 0 if the input list is empty.
        """
        if not nums:
            return 0

        max_length = 1
        current_length = 1

        # Check for strictly increasing subarray
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                current_length += 1
            else:
                max_length = max(max_length, current_length)
                current_length = 1
        max_length = max(max_length, current_length)

        current_length = 1

        # Check for strictly decreasing subarray
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                current_length += 1
            else:
                max_length = max(max_length, current_length)
                current_length = 1
        max_length = max(max_length, current_length)

        return max_length