# Leetcode 2817: Minimum Absolute Difference Between Elements With Constraint
# https://leetcode.com/problems/minimum-absolute-difference-between-elements-with-constraint/
# Solved on 24th of June, 2025
import math
from sortedcontainers import SortedList


class Solution:
    def minAbsoluteDifference(self, nums: list[int], x: int) -> int:
        """
        Calculates the minimum absolute difference between two elements nums[i] and nums[j]
        such that abs(i - j) >= x.

        Args:
            nums: A list of integers.
            x: An integer representing the minimum absolute difference between indices.

        Returns:
            The minimum absolute difference found.
        """
        numElements = len(nums)

        if x == 0:
            return 0

        minDifference = math.inf
        sortedDataSet = SortedList()

        for i in range(x, numElements):
            sortedDataSet.add(nums[i - x])

            targetValue = nums[i]

            insertionPoint = sortedDataSet.bisect_left(targetValue)

            if insertionPoint < len(sortedDataSet):
                elementAtIndex = sortedDataSet[insertionPoint]
                difference = abs(elementAtIndex - targetValue)
                minDifference = min(minDifference, difference)

            if insertionPoint > 0:
                elementBeforeIndex = sortedDataSet[insertionPoint - 1]
                difference = abs(targetValue - elementBeforeIndex)
                minDifference = min(minDifference, difference)

            if minDifference == 0:
                return 0

        return int(minDifference)