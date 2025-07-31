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
        maxLen = 0
        zeroCount = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeroCount += 1

            while zeroCount > k:
                if nums[left] == 0:
                    zeroCount -= 1
                left += 1

            currentLen = right - left + 1
            maxLen = max(maxLen, currentLen)

        return maxLen