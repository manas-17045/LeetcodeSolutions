# Leetcode 3336: Find the Number of Subsequences With Equal GCD
# https://leetcode.com/problems/find-the-number-of-subsequences-with-equal-gcd/
# Solved on 14th of June, 2025
import math


class Solution:
    def subsequencePairCount(self, nums: list[int]) -> int:
        """
        Calculates the number of ordered pairs of non-empty subsequences (sub1, sub2)
        of nums such that the greatest common divisor (GCD) of the elements in sub1
        is equal to the GCD of the elements in sub2.

        Args:
            nums: A list of integers.

        Returns:
            The number of such ordered pairs of subsequences, modulo 10^9 + 7.
        """
        MOD = 10**9 + 7
        maxV = max(nums)

        V = maxV

        dp = [[0] * (V + 1) for _ in range(V + 1)]
        dp[0][0] = 1

        for v in nums:
            nDp = [row[:] for row in dp]
            for g1 in range(V + 1):
                row = dp[g1]
                for g2 in range(V + 1):
                    ways = row[g2]
                    if not ways:
                        continue
                    # Put v into subsequence1
                    ng1 = v if g1 == 0 else math.gcd(g1, v)
                    nDp[ng1][g2] = (nDp[ng1][g2] + ways) % MOD
                    # Put v into subsequence2
                    ng2 = v if g2 == 0 else math.gcd(g2, v)
                    nDp[g1][ng2] = (nDp[g1][ng2] + ways) % MOD

            dp = nDp

        # Sum over all g > 0 of dp[g][g]
        ans = 0
        for g in range(1, (V + 1)):
            ans = (ans + dp[g][g]) % MOD

        return ans