# Leetcode 1493: Longest Subarray of 1's After Deleting One Element
# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/
# Solved on 24th of August, 2025
class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        """
        Given a binary array nums, you should delete one element from it.
        Return the size of the longest non-empty subarray containing only 1's in the resulting array.
        Input: nums - a list of integers (0s and 1s)
        Output: an integer representing the length of the longest subarray of 1s after deleting one element.
        """
        left = 0
        zero_count = 0
        max_len = 0

        for right, v in enumerate(nums):
            if v == 0:
                zero_count += 1

            # Shrink window until we have at most one zero
            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            max_len = max(max_len, right - left + 1 - 1)

        return max_len