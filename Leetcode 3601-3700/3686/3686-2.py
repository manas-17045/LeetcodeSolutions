# Leetcode 3686: Number of Stable Subsequences
# https://leetcode.com/problems/number-of-stable-subsequences/
# Solved on 5th of October, 2025
class Solution:
    def countStableSubsequences(self, nums: list[int]) -> int:
        """
        Counts the number of stable subsequences in the given list of integers.
        :param nums: A list of integers.
        :return: The total count of stable subsequences modulo 10^9 + 7.
        """
        MOD = 10 ** 9 + 7

        dp = [0, 0, 0, 0]

        for num in nums:
            parity = num % 2
            new_dp = dp[:]

            if parity == 1:
                new_dp[0] = (new_dp[0] + 1) % MOD
                new_dp[2] = (new_dp[2] + dp[0]) % MOD
                new_dp[0] = (new_dp[0] + dp[1]) % MOD
                new_dp[0] = (new_dp[0] + dp[3]) % MOD

            else:
                new_dp[1] = (new_dp[1] + 1) % MOD
                new_dp[3] = (new_dp[3] + dp[1]) % MOD
                new_dp[1] = (new_dp[1] + dp[0]) % MOD
                new_dp[1] = (new_dp[1] + dp[2]) % MOD

            dp = new_dp

        return sum(dp) % MOD