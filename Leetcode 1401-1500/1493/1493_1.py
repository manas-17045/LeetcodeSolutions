# Leetcode 1493: Longest Subarray of 1's After Deleting One Element
# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/
# Solved on 24th of August, 2025
class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        """
        Given a binary array nums, you should delete one element from it.
        Return the size of the longest non-empty subarray containing only 1's in the resulting array.
        If there is no such subarray, return 0.

        Args:
            nums (list[int]): A binary array.
        Returns:
            int: The size of the longest subarray containing only 1's after deleting one element.
        """
        maxLength = 0
        leftPointer = 0
        zeroCount = 0

        for rightPointer in range(len(nums)):
            if nums[rightPointer] == 0:
                zeroCount += 1

            while zeroCount > 1:
                if nums[leftPointer] == 0:
                    zeroCount -= 1
                leftPointer += 1

            maxLength = max(maxLength, rightPointer - leftPointer)

        return maxLength