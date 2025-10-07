# Leetcode 2499: Minimum Total Cost to Make Arrays Unequal
# https://leetcode.com/problems/minimum-total-cost-to-make-arrays-unequal/
# Solved on 7th of October, 2025
import collections


class Solution:
    def minimumTotalCost(self, nums1: list[int], nums2: list[int]) -> int:
        """
        Calculates the minimum total cost to make arrays unequal.

        Args:
            nums1: The first list of integers.
            nums2: The second list of integers.
        Returns:
            The minimum total cost to make arrays unequal, or -1 if it's impossible.
        """
        n = len(nums1)
        totalCost = 0
        numSame = 0
        freqMap = collections.Counter()
        isSame = [False] * n

        for i in range(n):
            if nums1[i] == nums2[i]:
                totalCost += i
                numSame += 1
                val = nums1[i]
                freqMap[val] += 1
                isSame[i] = True

        if numSame == 0:
            return 0

        dominantValue, maxFreq = freqMap.most_common(1)[0]

        swapsToFind = 0
        if maxFreq > numSame / 2:
            swapsToFind = 2 * maxFreq - numSame

        if swapsToFind == 0:
            return totalCost

        for j in range(n):
            if swapsToFind == 0:
                break

            if not isSame[j] and nums1[j] != dominantValue and nums2[j] != dominantValue:
                totalCost += j
                swapsToFind -= 1

        if swapsToFind > 0:
            return -1

        return totalCost