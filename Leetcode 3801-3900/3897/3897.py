# Leetcode 3897: Maximum Value of Concatenated Binary Segments
# https://leetcode.com/problems/maximum-value-of-concatenated-binary-segments/
# Solved on 20th of April, 2026
class Solution:
    def maxValue(self, nums1: list[int], nums0: list[int]) -> int:
        """
        Calculates the maximum possible value of concatenated binary segments.

        :param nums1: A list of integers representing the count of '1's in each segment.
        :param nums0: A list of integers representing the count of '0's in each segment.
        :return: The maximum value of the concatenated binary string modulo 10^9 + 7.
        """
        segmentList = []
        for onesCount, zerosCount in zip(nums1, nums0):
            if zerosCount == 0:
                segmentList.append((0, 0, 0, onesCount, zerosCount))
            elif onesCount == 0:
                segmentList.append((2, 0, 0, onesCount, zerosCount))
            else:
                segmentList.append((1, -onesCount, zerosCount, onesCount, zerosCount))

        segmentList.sort()

        modVal = 10**9 + 7
        ansVal = 0

        for _, _, _, onesCount, zerosCount in segmentList:
            powOnes = pow(2, onesCount, modVal)
            powZeros = pow(2, zerosCount, modVal)
            ansVal = (ansVal * powOnes + powOnes - 1) % modVal
            ansVal = (ansVal * powZeros) % modVal

        return ansVal