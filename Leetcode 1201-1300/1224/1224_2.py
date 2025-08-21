# Leetcode 1224: Maximum Equal Frequency
# https://leetcode.com/problems/maximum-equal-frequency/
# Solved on 21st of August, 2025
from collections import defaultdict


class Solution:
    def maxEqualFreq(self, nums: list[int]) -> int:
        """
        Calculates the maximum length of a prefix of the given array such that
        after removing exactly one element from the prefix, all remaining elements have the same frequency.

        :param nums: A list of integers.
        :return: The maximum length of a valid prefix.
        """
        count = defaultdict(int)
        freqCount = defaultdict(int)

        res = 0
        maxFreq = 0

        for i, x in enumerate(nums, start=1):
            prev = count[x]
            if prev > 0:
                freqCount[prev] -= 1

            count[x] = prev + 1
            freqCount[prev + 1] += 1
            if prev + 1 > maxFreq:
                maxFreq = prev + 1

            if maxFreq == 1:
                res = i
            elif freqCount[1] == i and maxFreq * freqCount[maxFreq] + 1 == i:
                res = i
            elif freqCount[maxFreq] == 1 and (maxFreq * freqCount[maxFreq] + (maxFreq - 1) * freqCount.get(maxFreq - 1, 0) == i):
                res = i

        return res