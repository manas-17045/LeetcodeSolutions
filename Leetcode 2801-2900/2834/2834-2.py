# Leetcode 2834: Find the Minimum Possible Sum of a Beautiful Array
# https://leetcode.com/problems/find-the-minimum-possible-sum-of-a-beautiful-array/
# Solved on 7th of October, 2025
class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        """
        Calculates the minimum possible sum of n distinct positive integers such that no two integers sum up to the target.
        :param n: The number of distinct positive integers to select.
        :param target: The target sum that no two selected integers should equal.
        :return: The minimum possible sum of the n integers, modulo 10^9 + 7.
        """
        MOD = 10**9 + 7

        # Number of integers we can select from [1, target/2]
        half = target // 2

        if n // 2:
            return (n * (n + 1) // 2) % MOD
        else:
            sum1 = half * (half + 1) // 2

            remaining = n - half

            sum2 = remaining * target + remaining * (remaining - 1) // 2

            return (sum1 + sum2) % MOD