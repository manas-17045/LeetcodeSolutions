# Leetcode 1250: Check If It is a Good Array
# https://leetcode.com/problems/check-if-it-is-a-good-array/
# Solved on 7th of July, 2025
from functools import reduce
from math import gcd


class Solution:
    def isGoodArray(self, nums: list[int]) -> bool:
        """
        Given an array nums of positive integers, return true if and only if the greatest common divisor of all
        the integers in nums is 1.
        """
        return reduce(gcd, nums) == 1