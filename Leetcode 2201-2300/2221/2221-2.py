# Leetcode 2221: Find Triangular Sum of an Array
# https://leetcode.com/problems/find-triangular-sum-of-an-array/
# Solved on 9th of September, 2025
class Solution:
    def triangularSum(self, nums: list[int]) -> int:
        """
        Calculates the triangular sum of a list of numbers.
        :param nums: A list of integers.
        :return: The last digit of the triangular sum.
        """
        n = len(nums)
        res = 0
        coEff = 1

        for i in range(n):
            res = (res + coEff * nums[i]) % 10

            if i < (n - 1):
                coEff = coEff * (n - 1 - i) // (i + 1)

        return res