# Leetcode 1848: Minimum Distance to the Target Element
# https://leetcode.com/problems/minimum-distance0to-the-target-element/
# Solved on 13th of April, 2026
class Solution:
    def getMinDistance(self, nums: list[int], target: int, start: int) -> int:
        """
        Finds the minimum distance |i - start| such that nums[i] == target.

        :param nums: List of integers to search through.
        :param target: The integer value to find in the list.
        :param start: The starting index to calculate distance from.
        :return: The minimum absolute difference between a valid index i and start.
        """
        arrayLength = len(nums)
        for distance in range(arrayLength):
            rightIndex = start + distance
            if rightIndex < arrayLength and nums[rightIndex] == target:
                return distance

            leftIndex = start - distance
            if leftIndex >= 0 and nums[leftIndex] == target:
                return distance

        return 0