# Leetcode 1004: Max Consecutive Ones III
# https://leetcode.com/problems/max-consecutive-ones-iii/
# Solved on 31st of July, 2025
class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        """
        Finds the length of the longest subarray of consecutive ones,
        allowing to flip at most k zeros to ones.

        Args:
            nums: A list of integers (0s and 1s).
            k: The maximum number of zeros that can be flipped to ones.

        Returns:
            The length of the longest subarray of consecutive ones.
        """
        left = 0
        zeros = 0
        max_len = 0

        for right, v in enumerate(nums):
            # Expand window to the right
            if v == 0:
                zeros += 1

            # If we've used up more than k zero-flips, shrink from the left
            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            # Update best window size
            current_len = right - left + 1
            if current_len > max_len:
                max_len = current_len

        return max_len