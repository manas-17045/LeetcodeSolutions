# Leetcode 594: Longest Harmonious Subsequence
# https://leetcode.com/problems/longest-harmonious-subsequence/
# Solved on 30th of June, 2025
from collections import Counter


class Solution:
    def findLHS(self, nums: list[int]) -> int:
        """
        Finds the length of the longest harmonious subsequence in the given array.

        A harmonious subsequence is a subsequence where the difference between its
        maximum and minimum value is exactly 1.

        Args:
            nums: A list of integers.
        Returns:
            The length of the longest harmonious subsequence.
        """
        # Count how many times each number appears
        freq = Counter(nums)

        best = 0
        # For each distinct value, see if value + 1 is present
        for x in freq:
            if (x + 1) in freq:
                # A harmonious subsequence can only consist of x's and (x = 1)'s
                best = max(best, (freq[x] + freq[x + 1]))

        return best