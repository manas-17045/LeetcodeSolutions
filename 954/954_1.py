# Leetcode 954: Array of Doubled Pairs
# https://leetcode.com/problems/array-of-doubled-pairs/
# Solved on 5th of July, 2025
import collections


class Solution:
    def canReorderDoubled(self, arr: list[int]) -> bool:
        """
        Determines if the given array can be reordered such that for every element x,
        there exists an element 2x in the array, and these pairs cover all elements.

        Args:
            arr: A list of integers.
        Returns:
            True if the array can be reordered into doubled pairs, False otherwise.
        """
        valueCounts = collections.Counter(arr)

        if valueCounts.get(0, 0) % 2 != 0:
            return False

        sortedKeys = sorted([key for key in valueCounts if key != 0], key=abs)

        for num in sortedKeys:
            if valueCounts[num] == 0:
                continue

            targetNum = num * 2

            if valueCounts[num] > valueCounts.get(targetNum, 0):
                return False

            valueCounts[targetNum] -= valueCounts[num]

        return True