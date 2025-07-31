# Leetcode 2401: Longest Nice Subarray
# https://leetcode.com/problems/longest-nice-subarray/
# Solved on 31st of July, 2025
class Solution:
    def longestNiceSubarray(self, nums: list[int]) -> int:
        """
        Finds the length of the longest "nice" subarray.
        A subarray is considered "nice" if the bitwise AND of every pair of numbers in it is 0.
        This means no two numbers in the subarray share a common set bit.

        Args:
            nums: A list of integers.
        Returns:
            The length of the longest nice subarray.
        """
        # Bitwise OR of all numbers in the current window
        mask = 0
        # Left index of window
        left = 0
        # At least one element is always valid
        best = 1

        for right, x in enumerate(nums):
            # If x conflicts (shares any 1-bit) with the window, shrink from the left
            while mask & x:
                mask ^= nums[left]
                left += 1
            # Now, it's safe to include x
            mask |= x
            best = max(best, right - left + 1)

        return best