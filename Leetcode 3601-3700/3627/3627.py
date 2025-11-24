# Leetcode 3627: Maximum Median Sum of Subsequences of Size 3
# https://leetcode.com/problems/maximum-median-sum-of-subsequences-of-size-3/
# Solved on 24th of November, 2025
class Solution:
    def maximumMedianSum(self, nums: list[int]) -> int:
        """
        Calculates the maximum possible sum of medians from subsequences of size 3.

        :param nums: A list of integers.
        :return: The maximum median sum.
        """
        nums.sort()
        arrayLength = len(nums)
        startIndex = arrayLength // 3
        medianSum = 0
        for i in range(startIndex, arrayLength, 2):
            medianSum += nums[i]
        return medianSum