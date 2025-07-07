# Leetcode 1250: Check If It is a Good Array
# https://leetcode.com/problems/check-if-it-is-a-good-array/
# Solved on 7th of July, 2025
import math


class Solution:
    def isGoodArray(self, nums: list[int]) -> bool:
        """
        Given an array nums of positive integers, return true if there exists a subsequence of nums
        whose greatest common divisor is 1, otherwise return false.
        """
        resultGcd = nums[0]
        for i in range(1, len(nums)):
            resultGcd = math.gcd(resultGcd, nums[i])
            if resultGcd == 1:
                return True
        return resultGcd == 1