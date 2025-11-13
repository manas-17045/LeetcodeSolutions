# Leetcode 3020: Find the Maximum Number of Elements in Subset
# https://leetcode.com/problems/find-the-maximum-number-of-elements-in-subset/
# Solved on 13th of November, 2025
from collections import Counter


class Solution:
    def maximumLength(self, nums: list[int]) -> int:
        """
        Finds the maximum length of a subset where for every element x in the subset,
        x*x is also in the subset, and if x*x is in the subset, then x*x*x*x is also in the subset, and so on.

        :param nums: A list of integers.
        :return: The maximum length of such a subset.
        """
        freq = Counter(nums)
        maxLen = 0

        if freq[1] > 0:
            maxLen = freq[1]
            if maxLen % 2 == 0:
                maxLen -= 1

        for num in freq:
            if num == 1:
                continue

            currentLen = 0
            curr = num

            while freq[curr] >= 2:
                currentLen += 2
                curr = curr * curr

            if freq[curr] > 0:
                currentLen += 1
            else:
                currentLen -= 1

            if currentLen > maxLen:
                maxLen = currentLen

        return maxLen