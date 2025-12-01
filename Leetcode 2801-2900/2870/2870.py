# Leetcode 2870: Minimum Number of Operations to Make Array Empty
# https://leetcode.com/problems/minimum-number-of-operations-to-make-array-empty/
# Solved on 1st of December, 2025
from collections import Counter


class Solution:
    def minOperations(self, nums: list[int]) -> int:
        """
        Calculates the minimum number of operations to make the array empty.

        An operation consists of removing either 2 or 3 identical elements.

        Args:
            nums: A list of integers.
        Returns:
            The minimum number of operations, or -1 if it's impossible.
        """
        frequencyMap = Counter(nums)
        totalOperations = 0

        for frequency in frequencyMap.values():
            if frequency == 1:
                return -1
            totalOperations += (frequency + 2) // 3

        return totalOperations