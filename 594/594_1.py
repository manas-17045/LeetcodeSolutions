# Leetcode 594: Longest Harmonious Subsequence
# https://leetcode.com/problems/longest-harmonious-subsequence/
# Solved on 30th of June, 2025
from collections import Counter


class Solution:
    def findLHS(self, nums: list[int]) -> int:
        """
        Finds the length of the longest harmonious subsequence.

        A harmonious array is an array where the difference between its maximum and minimum value is exactly 1.
        A subsequence is a sequence that can be derived from another sequence by deleting some or no elements
        without changing the order of the remaining elements.

        :param nums: A list of integers.
        :return: The length of the longest harmonious subsequence.
        """
        numCounts = Counter(nums)
        longestLength = 0
        for num in numCounts:
            if (num + 1) in numCounts:
                currentLength = numCounts[num] + numCounts[num + 1]
                if currentLength > longestLength:
                    longestLength = currentLength
        return longestLength