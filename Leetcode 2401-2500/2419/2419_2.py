# Leetcode 2419: Longest Subarray With Maximum Bitwise AND
# https://leetcode.com/problem/longest-subarray-with-maximum-bitwise-and/
# Solved on 30th of July, 2025
class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        """
        Finds the length of the longest subarray where all elements are equal to the maximum element in the input array.

        Args:
            nums (list[int]): The input list of integers.
        Returns:
            int: The length of the longest subarray containing only the maximum element.
        """
        # Find the overall maximum element k
        k = max(nums)

        # Scan for the longest contiguous run of elements == k
        best = 0
        cur = 0
        for x in nums:
            if x == k:
                cur += 1
                # Update best whenever we extend the run
                if cur > best:
                    best = cur
            else:
                # Reset when we hit something < k
                cur = 0

        return best