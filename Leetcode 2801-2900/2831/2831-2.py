# Leetcode 2831: Find the Longest Equal Subarray
# https://leetcode.com/problems/find-the-longest-equal-subarray/
# Solved on 26th of August, 2025
from collections import defaultdict


class Solution:
    def longestEqualSubarray(self, nums: list[int], k: int) -> int:
        """
        Finds the length of the longest equal subarray after deleting at most k elements.

        Args:
            nums: A list of integers.
            k: The maximum number of elements that can be deleted.
        Returns:
            The length of the longest equal subarray.
        """
        # Map each value to the list of indices where it appears
        pos = defaultdict(list)
        for i, v in enumerate(nums):
            pos[v].append(i)

        ans = 0
        # For each value, use sliding window on its positions
        for indices in pos.values():
            l = 0
            for r in range(len(indices)):
                # While deletions required exceed k, move left pointer
                while l <= r and (indices[r] - indices[l] - (r - l)) > k:
                    l += 1
                # Number of equal elements we can keep in this window
                ans = max(ans, r - l + 1)

        return ans