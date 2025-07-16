# Leetcode 3539: Find Sum of Array Product of Magical Sequences
# https://leetcode.com/problems/find-sum-of-array-product-of-magical-sequences/
# Solved on 16th of July, 2025
import sys
from functools import lru_cache


class Solution:
    def magicalSum(self, m: int, k: int, nums: list[int]) -> int:
        """
        Calculates the magical sum based on given parameters.

        The problem asks to find the sum of products of chosen numbers,
        such that the sum of their indices (when represented in binary)
        has exactly `k` set bits.

        Args:
            m (int): The total number of elements to choose.
            k (int): The required number of set bits in the binary sum of chosen indices.
            nums (list[int]): A list of numbers from which to choose.

        Returns:
            int: The magical sum modulo 10^9 + 7.
        """
        MOD = 10**9 + 7
        n = len(nums)

        # Precompute C(n, r) for n, r up to m
        comb = [[0] * (m + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            comb[i][0] = 1
            for j in range(1, i + 1):
                comb[i][j] = (comb[i - 1][j - 1] + comb[i - 1][j]) % MOD

        sys.setrecursionlimit(10**7)

        @lru_cache(None)
        def dp(i: int, rem: int, bits_left: int, carry: int) -> int:
            if rem < 0 or bits_left < 0 or (rem + carry.bit_count() < bits_left):
                return 0

            if rem == 0:
                return 1 if bits_left == carry.bit_count() else 0

            if i == n:
                return 0

            res = 0
            for cnt in range(rem + 1):
                # Ways to choose cnt positions among rem
                ways = comb[rem][cnt]
                p = pow(nums[i], cnt, MOD)

                new_carry = carry + cnt
                lsb = new_carry & 1
                # For next bit-column, carry shifts right
                next_carry = new_carry >> 1

                res += ways * p % MOD * dp((i + 1), rem - cnt, bits_left - lsb, next_carry)
                res %= MOD

            return res

        return dp(0, m, k, 0)