# Leetcode 3649: Number of Perfect Pairs
# https://leetcode.com/problems/number-of-perfect-pairs/
# Solved on 29th of December, 2025
class Solution:
    def perfectPairs(self, nums: list[int]) -> int:
        """
        Calculates the number of "perfect pairs" in a given list of integers.
        A pair (nums[i], nums[j]) is considered perfect if abs(nums[i]) * 2 >= abs(nums[j])
        and i < j.
        :param nums: A list of integers.
        :return: The total count of perfect pairs.
        """
        sortedAbsNums = sorted([abs(x) for x in nums])
        perfectPairsCount = 0
        leftIndex = 0
        arrayLength = len(sortedAbsNums)

        for rightIndex in range(arrayLength):
            currentNum = sortedAbsNums[rightIndex]
            while leftIndex < rightIndex and sortedAbsNums[leftIndex] * 2 < currentNum:
                leftIndex += 1
            perfectPairsCount += rightIndex - leftIndex

        return perfectPairsCount