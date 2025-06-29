# Leetcode 3082: Find the Sum of the Power of All Subsequences
# https://leetcode.com/problems/find-the-sum-of-the-power-of-all-subsequences/
# Solved on 29th of June, 2025
class Solution:
    def sumOfPower(self, nums: list[int], k: int) -> int:
        """
        Calculates the sum of powers of all subsequences where the sum of elements in the subsequence equals k.
        The power of a subsequence is defined as 2^(number of elements not in the subsequence).
        """
        MOD = 10**9 + 7
        n = len(nums)
        # Inverse of 2 mod MOD
        inv2 = pow(2, (MOD - 2), MOD)

        dp = [0] * (k + 1)
        dp[0] = 1

        for v in nums:
            # Update backwards so each item is used at most once
            for s in range(k, (v - 1), -1):
                dp[s] = (dp[s] + (dp[s - v] * inv2)) % MOD

        return dp[k] * pow(2, n, MOD) % MOD