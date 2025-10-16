# Leetcode 2856: Minimum Array Length After Pair Removals
# https://leetcode.com/problems/minimum-array-length-after-pair-removals/
# Solved on 16th of October, 2025
from collections import Counter


class Solution:
    def minLengthAfterRemovals(self, nums: list[int]) -> int:
        """
        Calculates the minimum length of the array after performing removals.
        :param nums: A list of integers.
        :return: The minimum possible length of the array after removals.
        """
        n = len(nums)

        # Count frequency of each number
        freq_map = Counter(nums)

        # Get the maximum frequency
        max_frequency = max(freq_map.values())

        return max(n % 2, 2 * max_frequency - n)