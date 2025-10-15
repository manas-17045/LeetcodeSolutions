# Leetcode 3034: Number of Subarrays That Match a Pattern I
# https://leetcode.com/problems/number-of-subarrays-that-match-a-pattern-i/
# Solved on 15th of October, 2025
class Solution:
    def countMatchingSubarrays(self, nums: list[int], pattern: list[int]) -> int:
        """
        Counts the number of subarrays in `nums` that match the given `pattern`.

        A subarray matches the pattern if the relative order of its adjacent elements
        (increasing, decreasing, or equal) corresponds to the pattern elements (1, -1, or 0).

        Args:
            nums (list[int]): The input array of integers.
            pattern (list[int]): The pattern to match, where 1 means increasing, -1 means decreasing, and 0 means equal.

        Returns:
            int: The total number of matching subarrays.
        """
        n = len(nums)
        m = len(pattern)
        if n < 2 or m == 0:
            return 0

        diffs = [1 if nums[i + 1] > nums[i] else 0 if nums[i + 1] == nums[i] else -1 for i in range(n - 1)]

        # If pattern is longer than diffs, no matches possible
        if m > len(diffs):
            return 0

        count = 0

        # Slide window over diffs and compare element-wise (avoid creating slices repeatedly)
        last_start = len(diffs) - m
        for start in range(last_start + 1):
            match = True
            for j in range(m):
                if diffs[start + j] != pattern[j]:
                    match = False
                    break
            if match:
                count += 1

        return count