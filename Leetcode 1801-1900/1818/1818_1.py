# Leetcode 181: Minimum Absolute Sum Difference
# https://leetcode.com/problems/minimum-absolute-sum-difference/
# Solved on 23rd of August, 2025
import bisect


class Solution:
    def minAbsoluteSumDiff(self, nums1: list[int], nums2: list[int]) -> int:
        """
        Calculates the minimum absolute sum difference by potentially replacing one element in nums1.

        The goal is to minimize sum(|nums1[i] - nums2[i]|) by replacing at most one element in nums1
        with another element from nums1.

        :param nums1: A list of integers.
        :param nums2: A list of integers of the same length as nums1.
        :return: The minimum absolute sum difference modulo 10^9 + 7.
        """
        n = len(nums1)
        mod = 10 ** 9 + 7

        sortedNums1 = sorted(nums1)

        initialSum = sum(abs(n1 - n2) for n1, n2 in zip(nums1, nums2))

        if initialSum == 0:
            return 0

        maxReduction = 0
        for i in range(n):
            originalDiff = abs(nums1[i] - nums2[i])
            target = nums2[i]

            insertionPoint = bisect.bisect_left(sortedNums1, target)

            minNewDiff = float('inf')

            if insertionPoint < n:
                candidate = sortedNums1[insertionPoint]
                minNewDiff = min(minNewDiff, abs(candidate - target))

            if insertionPoint > 0:
                candidate = sortedNums1[insertionPoint - 1]
                minNewDiff = min(minNewDiff, abs(candidate - target))

            currentReduction = originalDiff - minNewDiff
            maxReduction = max(maxReduction, currentReduction)

        finalSum = initialSum - maxReduction

        return finalSum % mod