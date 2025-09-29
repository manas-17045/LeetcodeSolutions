# Leetcode 2897: Apply Operations on Array to Maximize Sum of Squares
# https://leetcode.com/problems/apply-operations-on-array-to-maximize-sum-of-squares/
# Solved on 29th of September, 2025
class Solution:
    def maxSum(self, nums: list[int], k: int) -> int:
        """
        Calculates the maximum possible sum of squares of k numbers, where these k numbers are formed by
        greedily assigning bits from the input `nums` to maximize the sum.

        :param nums: A list of integers.
        :param k: The number of integers to form.
        :return: The maximum sum of squares modulo 10^9 + 7.
        """
        MOD = 10**9 + 7

        # Find highest bit needed
        max_bit = 0
        for x in nums:
            if x.bit_length() > max_bit:
                max_bit = x.bit_length()

        # Count how many times each bit is set across all numbers
        cnt = [0] * max_bit
        for x in nums:
            b = 0
            while x:
                if x & 1:
                    cnt[b] += 1
                x >>= 1
                b += 1

        # Greedily construct k numbers by taking the highest available bits first
        res = 0
        for _ in range(k):
            val = 0
            # Assign available bits from most significant to least
            for b in range(max_bit - 1, -1, -1):
                if cnt[b] > 0:
                    val |= (1 << b)
                    cnt[b] -= 1
            res = (res + (val * val)) % MOD

        return res