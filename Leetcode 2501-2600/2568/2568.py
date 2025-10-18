# Leetcode 2568: Minimum Impossible OR
# https://leetcode.com/problems/minimum-impossible-or/
# Solved on 18th of October, 2025
class Solution:
    def minImpossibleOR(self, nums: list[int]) -> int:

        numSet = set(nums)
        powerOfTwo = 1

        while powerOfTwo in numSet:
            powerOfTwo <<= 1

        return powerOfTwo