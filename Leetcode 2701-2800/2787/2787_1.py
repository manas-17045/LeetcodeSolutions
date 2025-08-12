# Leetcode 2787: Ways to Express an Integer as Sum of Powers
# https://leetcode.com/problems/ways-to-express-an-integer-as-sum-of-powers/
# Solved on 12th of August, 2025
class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        """
        Calculates the number of ways to express an integer 'n' as the sum of unique positive integers,
        each raised to the power 'x'.

        Args:
            n (int): The target integer.
            x (int): The power to which each unique positive integer is raised.
        Returns:
            int: The number of ways to express 'n' as the sum of unique powers, modulo 10^9 + 7.
        """
        mod = 10**9 + 7
        dp = [0] * (n + 1)
        dp[0] = 1

        num = 1
        while True:
            power = num**x
            if power > n:
                break

            for i in range(n, (power - 1), -1):
                dp[i] = (dp[i] + dp[i - power]) % mod

            num += 1

        return dp[n]