# Leetcode 1909: Remove One Element to Make the Array Strictly Increasing
# https://leetcode.com/problems/remove-one-element-to-make-the-array-strictly-increasing/
# Solved on 5th of September, 2025
class Solution:
    def canBeIncreasing(self, nums: list[int]) -> bool:
        """
        Checks if an array can be made strictly increasing by removing at most one element.

        Args:
            nums: A list of integers.
        Returns:
            True if the array can be made strictly increasing, False otherwise.
        """
        dipCount = 0
        violationIndex = -1
        listLength = len(nums)

        for i in range(1, listLength):
            if nums[i - 1] >= nums[i]:
                dipCount += 1
                violationIndex = i

        if dipCount == 0:
            return True

        if dipCount > 1:
            return False

        fixByRemovingPrev = False
        if violationIndex == 1 or nums[violationIndex - 2] < nums[violationIndex]:
            fixByRemovingPrev = True

        fixByRemovingCurr = False
        if violationIndex == listLength - 1 or nums[violationIndex - 1] < nums[violationIndex + 1]:
            fixByRemovingCurr = True

        return fixByRemovingPrev or fixByRemovingCurr