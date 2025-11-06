# Leetcode 3587: Minimum Adjacent Swaps to Alternate Parity
# https://leetcode.com/problems/minimum-adjacent-swaps-to-alternate-parity/
# Solved on 6th of November, 2025
class Solution:
    def minSwaps(self, nums: list[int]) -> int:
        """
        Calculates the minimum number of adjacent swaps required to arrange the array
        such that elements alternate in parity (even, odd, even, odd, ... or odd, even, odd, even, ...).

        :param nums: A list of integers.
        :return: The minimum number of swaps, or -1 if it's not possible to achieve alternating parity.
        """
        evenIndices = []
        oddIndices = []

        for i, num in enumerate(nums):
            if num % 2 == 0:
                evenIndices.append(i)
            else:
                oddIndices.append(i)

        countEven = len(evenIndices)
        countOdd = len(oddIndices)

        if abs(countEven - countOdd) > 1:
            return -1

        swaps1 = float('inf')
        swaps2 = float('inf')

        if countEven >= countOdd:
            swaps1 = 0
            for i in range(countEven):
                targetIndex = i * 2
                swaps1 += abs(evenIndices[i] - targetIndex)

        if countOdd >= countEven:
            swaps2 = 0
            for i in range(countEven):
                targetIndex = i * 2 + 1
                swaps2 += abs(evenIndices[i] - targetIndex)

        return min(swaps1, swaps2)