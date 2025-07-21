# Leetcode 3317: Find the Number of Possible Ways for an Event
# https://leetcode.com/problems/find-the-number-of-possible-ways-for-an-event/
# Solved on 21st of July, 2025
class Solution:
    def numberOfWays(self, n: int, x: int, y: int) -> int:
        """
        Calculates the number of ways to distribute n distinct items into x distinct boxes,
        where each box can contain at most one item, and each item has a weight y.

        Args:
            n (int): The number of distinct items.
            x (int): The number of distinct boxes.
            y (int): The weight associated with each item.

        Returns:
            int: The number of ways to distribute the items modulo 10^9 + 7.
        """
        MOD = 10**9 + 7

        dp = [0] * (x + 1)
        dp[0] = 1

        # Build up Stirling numbers
        for i in range(1, n + 1):
            new = [0] * (x + 1)
            upper = min(i, x)
            for j in range(1, (upper + 1)):
                new[j] = (dp[j] * j + dp[j - 1]) % MOD
            dp = new

        # Precompute falling factorials
        P = [1] * (x + 1)
        for k in range(1, (x + 1)):
            P[k] = P[k - 1] * (x - k + 1) % MOD

        yPow = [1] * (x + 1)
        for k in range(1, (x + 1)):
            yPow[k] = yPow[k - 1] * y % MOD

        # Sum up S(n, k) * P(x, k) * y^k for k = 1...min(n, x)
        ans = 0
        for k in range(1, (min(n, x) + 1)):
            ans = (ans + dp[k] * P[k] % MOD * yPow[k]) % MOD

        return ans