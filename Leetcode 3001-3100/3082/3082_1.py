# Leetcode 3082: Find the Sum of the Power of All Subsequences
# https://leetcode.com/problems/find-the-sum-of-the-power-of-all-subsequences/
# Solved on 29th of June, 2025
class Solution:
    def sumOfPower(self, nums: list[int], k: int) -> int:
        """
        Calculates the sum of powers of all possible subsequences of `nums` whose sum is `k`.

        For each subsequence, its power is defined as 2^(n - len(subsequence)) * sum(subsequence).
        The problem asks for the sum of powers of all subsequences whose sum is exactly `k`.

        Args:
            nums: A list of integers.
            k: The target sum.
        Returns:
            The sum of powers modulo 10^9 + 7.
        """
        n = len(nums)
        mod = 1_000_000_007

        dp = [0] * (k + 1)
        dp[0] = 1

        invTwo = pow(2, (mod - 2), mod)

        for num in nums:
            for j in range(k, (num - 1), -1):
                term = (dp[j - num] * invTwo) % mod
                dp[j] = (dp[j] + term) % mod

        powTwoN = pow(2, n, mod)

        result = (dp[k] * powTwoN) % mod

        return result