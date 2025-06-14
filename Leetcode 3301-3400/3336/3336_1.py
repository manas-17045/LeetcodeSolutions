# Leetcode 3336: Find the Number of Subsequences With Equal GCD
# https://leetcode.com/problems/find-the-number-of-subsequences-with-equal-gcd/
# Solved on 14th of June, 2025
import math
from collections import defaultdict


class Solution:
    def subsequencePairCount(self, nums: list[int]) -> int:
        """
        Finds the number of pairs of non-empty subsequences of nums such that the GCD of the first subsequence
        is equal to the GCD of the second subsequence.

        Args:
            nums: A list of integers.

        Returns:
            The number of such pairs of subsequences, modulo 10^9 + 7.
        """
        mod = 10**9 + 7

        dp = defaultdict(int)
        dp[(0, 0)] = 1

        for x in nums:
            newDp = defaultdict(int)
            for (g1, g2), count in dp.items():
                newDp[(g1, g2)] = (newDp[(g1, g2)] + count) % mod

                newG1 = x if g1 == 0 else math.gcd(g1, x)
                newDp[(newG1, g2)] = (newDp[(newG1, g2)] + count) % mod

                newG2 = x if g2 == 0 else math.gcd(g2, x)
                newDp[(g1, newG2)] = (newDp[(g1, newG2)] + count) % mod

            dp = newDp

        totalPairs = 0
        for (g1, g2), count in dp.items():
            if g1 > 0 and g1 == g2:
                totalPairs = (totalPairs + count) % mod

        return totalPairs