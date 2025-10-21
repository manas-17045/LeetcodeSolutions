# Leetcode 2654: Minimum Number of Operations to Make All Array Elements Equal to 1
# https://leetcode.com/problems/minimum-number-of-operations-to-make-all-array-elements-equal-to-1/
# Solved on 21st of October, 2025
import math


class Solution:
    def minOperations(self, nums: list[int]) -> int:
        """
        Calculates the minimum number of operations to make all array elements equal to 1.

        Args:
            nums: A list of integers.
        Returns:
            The minimum number of operations, or -1 if it's impossible.
        """
        arrLength = len(nums)

        onesCount = 0
        for num in nums:
            if num == 1:
                onesCount += 1

        if onesCount > 0:
            return arrLength - onesCount

        minSubarrayLength = float('inf')

        for i in range(arrLength):
            currentGCD = nums[i]
            for j in range(i, arrLength):
                currentGCD = math.gcd(currentGCD, nums[j])
                if currentGCD == 1:
                    currentLength = j - i + 1
                    minSubarrayLength = min(minSubarrayLength, currentLength)
                    break

        if minSubarrayLength == float('inf'):
            return -1

        return (minSubarrayLength - 1) + (arrLength - 1)