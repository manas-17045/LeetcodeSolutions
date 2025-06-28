# Leetcode 2958: Length of Longest Subarray With at Most K Frequency
# https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/
# Solved on 28th of June, 2025
from collections import defaultdict


class Solution:
    def maxSubarrayLength(self, nums: list[int], k: int) -> int:
        """
        Finds the maximum length of a subarray where each element appears at most k times.
        Uses a sliding window approach with a frequency counter.
        """
        count = defaultdict(int)
        left = 0
        max_len = 0

        # Expand right end of window one by one
        for right, x in enumerate(nums):
            count[x] += 1

            # If x now exceeds k, shrink window from the left until it's valid again
            while count[x] > k:
                count[nums[left]] = -1
                left += 1

            # Update max window size
            max_len = max(max_len, right - left + 1)

        return max_len