# Leetcode 2831: Find the Longest Equal Subarray
# https://leetcode.com/problems/find-the-longest-equal-subarray/
# Solved on 26th of August, 2025
import collections


class Solution:
    def longestEqualSubarray(self, nums: list[int], k: int) -> int:
        """
        Finds the length of the longest equal subarray such that at most k elements are removed.

        Args:
            nums: A list of integers.
            k: The maximum number of elements that can be removed.
        Returns:
            The length of the longest equal subarray.
        """
        counts = collections.defaultdict(int)
        left = 0
        maxFreq = 0

        for right, num in enumerate(nums):
            counts[num] += 1
            maxFreq = max(maxFreq, counts[num])

            if (right - left + 1) - maxFreq > k:
                leftNum = nums[left]
                counts[leftNum] -= 1
                left += 1

        return maxFreq