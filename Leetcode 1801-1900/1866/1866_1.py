# Leetcode 1866: Number of Ways to Rearrange Sticks With K Sticks Visible
# https://leetcode.com/problems/number-of-ways-to-rearrange-sticks-with-k-sticks-visible/
# Solved on 18th of August, 2025
class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        """
        Calculates the number of ways to arrange `n` sticks such that exactly `k` sticks are visible from the left.

        Args:
            n (int): The total number of sticks.
            k (int): The number of visible sticks required.
        Returns:
            int: The number of ways to arrange the sticks, modulo 10^9 + 7.
        """
        dp = [0] * (k + 1)
        dp[0] = 1
        mod = 10**9 + 7

        for i in range(1, n + 1):
            for j in range(k, 0, -1):
                dp[j] = (dp[j - 1] + dp[j] * (i - 1)) % mod
            dp[0] = 0

        return dp[k]