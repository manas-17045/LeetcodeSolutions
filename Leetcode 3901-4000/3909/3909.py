# Leetcode 3909: Compare Sums of Bitonic Parts
# https://leetcode.com/problems/compare-sums-of-bitonic-parts/
# Solved on 3rd of May, 2026
class Solution:
    def compareBitonicSums(self, nums: list[int]) -> int:
        """
        Compares the sum of the ascending part and the descending part of a bitonic array.

        :param nums: A list of integers representing a bitonic sequence.
        :return: 0 if ascending sum > descending sum, 1 if descending sum > ascending sum, else -1.
        """
        arrayLen = len(nums)
        ascSum = nums[0]
        currIndex = 1

        while currIndex < arrayLen and nums[currIndex] > nums[currIndex - 1]:
            ascSum += nums[currIndex]
            currIndex += 1

        descSum = nums[currIndex - 1]

        while currIndex < arrayLen:
            descSum += nums[currIndex]
            currIndex += 1

        return 0 if ascSum > descSum else 1 if descSum > ascSum else -1