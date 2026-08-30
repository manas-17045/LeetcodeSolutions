# Leetcode 2091: Removing Minimum and Maximum From Array
# https://leetcode.com/problems/removing-minimum-and-maximum-from-array/
# Solved on 30th of August, 2026
class Solution:
    def minimumDeletions(self, nums: list[int]) -> int:
        """
        Calculates the minimum number of deletions from the front and back of the array
        to remove both the minimum and maximum elements.

        Parameters:
        nums (list[int]): A 0-indexed list of distinct integers.

        Returns:
        int: The minimum number of deletions required.
        """
        arrayLength = len(nums)
        minIndex = 0
        maxIndex = 0

        for currentIndex in range(1, arrayLength):
            if nums[currentIndex] < nums[minIndex]:
                minIndex = currentIndex
            if nums[currentIndex] > nums[maxIndex]:
                maxIndex = currentIndex

        leftIndex = min(minIndex, maxIndex)
        rightIndex = max(minIndex, maxIndex)

        bothFront = rightIndex + 1
        bothBack = arrayLength - leftIndex
        bothSides = (leftIndex + 1) + (arrayLength - rightIndex)

        return min(bothFront, bothBack, bothSides)