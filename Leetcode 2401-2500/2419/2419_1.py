# Leetcode 2419: Longest Subarray With Maximum Bitwise AND
# https://leetcode.com/problem/longest-subarray-with-maximum-bitwise-and/
# Solved on 30th of July, 2025
class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        """
        Finds the length of the longest subarray such that all elements in the subarray
        are equal to the maximum element in the entire array.

        Args:
            nums: A list of integers.
        Returns:
            The length of the longest subarray with the maximum bitwise AND.
        """
        if not nums:
            return 0

        maxNum = max(nums)

        maxLength = 0
        currentLength = 0

        for num in nums:
            if num == maxNum:
                currentLength += 1
            else:
                maxLength = max(maxLength, currentLength)
                currentLength = 0

        maxLength = max(maxLength, currentLength)

        return maxLength