# Leetcode 2344: Minimum Deletions to Make Array Divisible
# https://leetcode.com/problems/minimum-deletions-to-make-array-divisible/
# Solved on 16th of August, 2025
import math


class Solution:
    def minOperations(self, nums: list[int], numsDivide: list[int]) -> int:
        """
        Calculates the minimum number of deletions required from `nums` such that the smallest remaining element
        divides all elements in `numsDivide`.

        :param nums: A list of integers.
        :param numsDivide: A list of integers that all remaining elements in `nums` must divide.
        :return: The minimum number of deletions, or -1 if no such element exists.
        """
        # Calculate the Greatest Common Divisor (GCD) of all elements in numsDivide.
        greatestCommonDivisor = numsDivide[0]
        for i in range(1, len(numsDivide)):
            greatestCommonDivisor = math.gcd(greatestCommonDivisor, numsDivide[i])

        # Sort the nums array to find the smallest suitable element first.
        nums.sort()

        # Find the first element in the sorted nums that divides the GCD.
        for i in range(len(nums)):
            if nums[i] % greatestCommonDivisor == 0:
                return i

        return -1  # If no suitable element is found, return -1.