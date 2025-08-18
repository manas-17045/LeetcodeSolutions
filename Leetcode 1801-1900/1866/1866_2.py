# Leetcode 1866: Number of Ways to Rearrange Sticks With K Sticks Visible
# https://leetcode.com/problems/number-of-ways-to-rearrange-sticks-with-k-sticks-visible/
# Solved on 18th of August, 2025
class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        """
        Calculates the number of ways to arrange `n` sticks of distinct lengths such that exactly `k` sticks are visible from the left.

        Args:
            n (int): The total number of sticks.
            k (int): The number of sticks that must be visible from the left.
        Returns:
            int: The number of ways to arrange the sticks modulo 10^9 + 7.
        """
        MOD = 10**9 + 7
        if k > n or k <= 0:
            return 0

        dp = [0] * (k + 1)
        dp[1] = 1

        for i in range(2, n + 1):
            # Compute dp for size i into new_dp
            new_dp = [0] * (k + 1)
            # j cannot exceed i
            upper = min(i, k)
            for j in range(1, upper + 1):
                add_new_visible = dp[j - 1]
                keep_visible = (dp[j] * (i - 1)) % MOD
                new_dp[j] = (add_new_visible + keep_visible) % MOD
            dp = new_dp

        return dp[k]