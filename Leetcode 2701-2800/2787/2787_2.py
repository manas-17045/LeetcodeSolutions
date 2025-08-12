# Leetcode 2787: Ways to Express an Integer as Sum of Powers
# https://leetcode.com/problems/ways-to-express-an-integer-as-sum-of-powers/
# Solved on 12th of August, 2025
class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        """
        Calculates the number of ways to express n as a sum of unique positive integers, each raised to the power of x.
        :param n: The target sum.
        :param x: The power to which each integer is raised.
        :return: The number of ways to form the sum n, modulo 10^9 + 7.
        """
        MOD = 10**9 + 7

        # Build list of k^x values <= n
        powers = []
        k = 1
        while True:
            val = k ** x
            if val > n:
                break
            powers.append(val)
            k += 1

        # dp[s] = number of way to get sum s using considered powers
        dp = [0] * (n + 1)
        dp[0] = 1

        # For each power, update dp backwards (0/1 knapsack)
        for p in powers:
            for s in range(n, p - 1, -1):
                dp[s] = (dp[s] + dp[s - p]) % MOD

        return dp[n]