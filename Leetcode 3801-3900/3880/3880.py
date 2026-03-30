# Leetcode 3880: Minimum Absolute Difference Between Two Values
# https://leetcode.com/problems/minimum-absolute-difference-between-two-values/
# Solved on 30th of March, 2026
class Solution:
    def minAbsoluteDifference(self, nums: list[int]) -> int:
        """
        Finds the minimum absolute difference between the indices of the values 1 and 2 in the list.

        :param nums: A list of integers containing values including 1s and 2s.
        :return: The minimum index difference between any 1 and any 2, or -1 if one is missing.
        """
        minDiff = float('inf')
        lastOne = -1
        lastTwo = -1

        for i in range(len(nums)):
            if nums[i] == 1:
                lastOne = i
                if lastTwo != -1:
                    minDiff = min(minDiff, i - lastTwo)
            elif nums[i] == 2:
                lastTwo = i
                if lastOne != -1:
                    minDiff = min(minDiff, i - lastOne)

        return -1 if minDiff == float('inf') else minDiff