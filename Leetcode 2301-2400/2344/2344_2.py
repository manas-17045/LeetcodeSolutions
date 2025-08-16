# Leetcode 2344: Minimum Deletions to Make Array Divisible
# https://leetcode.com/problems/minimum-deletions-to-make-array-divisible/
# Solved on 16th of August, 2025
from functools import reduce
import math


class Solution:
    def minOperations(self, nums: list[int], numsDivide: list[int]) -> int:
        """
        Finds the minimum number of operations to remove elements from `nums` such that the smallest remaining element divides all elements in `numsDivide`.
        :param nums: A list of integers.
        :param numsDivide: A list of integers that must be divisible by the chosen element from `nums`.
        :return: The minimum number of operations (elements removed) or -1 if no such element exists.
        """
        gcd_all = reduce(math.gcd, numsDivide)

        nums.sort()

        for i, val in enumerate(nums):
            if gcd_all % val == 0:
                return i

        return -1