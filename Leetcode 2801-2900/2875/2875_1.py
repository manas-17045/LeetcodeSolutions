# Leetcode 2875: Minimum Size Subarray in Infinite Array
# https://leetcode.com/problems/minimum-size-subarray-in-infinite-array/
# Solved on 20th of August, 2025
import math


class Solution:
    def minSizeSubarray(self, nums: list[int], target: int) -> int:
        """
        Finds the minimum size subarray in an infinite array (formed by repeating `nums`) that sums up to `target`.

        Args:
            nums (list[int]): The original array of integers.
            target (int): The target sum.
        Returns:
            int: The minimum length of a subarray that sums to `target`, or -1 if no such subarray exists.
        """
        totalSum = sum(nums)
        n = len(nums)

        numCopies = target // totalSum
        remTarget = target % totalSum

        minLengthRem = math.inf
        if remTarget == 0:
            minLengthRem = 0

        minLengthTarget = math.inf

        prefixSumMap = {0: -1}
        currentSum = 0

        doubleNums = nums + nums

        for i, val in enumerate(doubleNums):
            currentSum += val

            # Check for remainder target
            if remTarget != 0 and (currentSum - remTarget) in prefixSumMap:
                length = i - prefixSumMap[currentSum - remTarget]
                minLengthRem = min(minLengthRem, length)

            # Check for original target
            if (currentSum - target) in prefixSumMap:
                length = i - prefixSumMap[currentSum - target]
                minLengthTarget = min(minLengthTarget, length)

            if currentSum not in prefixSumMap:
                prefixSumMap[currentSum] = i

        result = minLengthTarget

        if minLengthRem != math.inf:
            result = min(result, numCopies * n + minLengthRem)

        return result if result != math.inf else -1