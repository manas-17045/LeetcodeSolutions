# Leetcode 3164: Find the Number of Good Pairs II
# https://leetcode.com/problems/find-the-number-of-good-pairs-ii/
# Solved on 25th of October, 2025
import collections


class Solution:
    def numberOfPairs(self, nums1: list[int], nums2: list[int], k: int) -> int:
        """
        Finds the number of good pairs (i, j) such that nums1[i] is divisible by nums2[j] * k.
        :param nums1: A list of integers.
        :param nums2: A list of integers.
        :param k: An integer.
        :return: The total number of good pairs.
        """
        maxNum = 0
        for val in nums1:
            if val > maxNum:
                maxNum = val

        num1Freq = collections.Counter(nums1)
        multiplesCount = [0] * (maxNum + 1)

        for val in range(1, maxNum + 1):
            for multiple in range(val, maxNum + 1, val):
                multiplesCount[val] += num1Freq.get(multiple, 0)

        totalPairs = 0

        for num2Val in nums2:
            targetDivisor = num2Val * k
            if targetDivisor <= maxNum:
                totalPairs += multiplesCount[targetDivisor]

        return totalPairs