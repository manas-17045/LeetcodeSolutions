# Leetcode 2856: Minimum Array Length After Pair Removals
# https://leetcode.com/problems/minimum-array-length-after-pair-removals/
# Solved on 16th of October, 2025
import collections


class Solution:
    def minLengthAfterRemovals(self, nums: list[int]) -> int:
        """
        Calculates the minimum length of the array after performing pair removals.

        :param nums: A list of integers.
        :return: The minimum possible length of the array after removals.
        """
        listLength = len(nums)
        if listLength == 0:
            return 0

        freqCounter = collections.Counter(nums)
        maxFrequency = freqCounter.most_common(1)[0][1]

        return (listLength % 2) if maxFrequency <= listLength // 2 else (2 * maxFrequency - listLength)