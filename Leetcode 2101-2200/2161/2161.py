# Leetcode 2161: Partition Array According to Given Pivot
# https://leetcode.com/problems/partition-array-according-to-given-pivot/
# Solved on 8th of June, 2026
class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        """
        Rearranges the array such that elements less than pivot come first,
        followed by elements equal to pivot, and then elements greater than pivot,
        preserving the relative order of elements within each group.

        :param nums: List of integers to be partitioned.
        :param pivot: The integer value to partition around.
        :return: A new list containing the partitioned elements.
        """
        lessCount = 0
        equalCount = 0
        for currentNum in nums:
            if currentNum < pivot:
                lessCount += 1
            elif currentNum == pivot:
                equalCount += 1

        resultArray = [0] * len(nums)
        lessIndex = 0
        equalIndex = lessCount
        greaterIndex = lessCount + equalCount

        for currentNum in nums:
            if currentNum < pivot:
                resultArray[lessIndex] = currentNum
                lessIndex += 1
            elif currentNum == pivot:
                resultArray[equalIndex] = currentNum
                equalIndex += 1
            else:
                resultArray[greaterIndex] = currentNum
                greaterIndex += 1

        return resultArray