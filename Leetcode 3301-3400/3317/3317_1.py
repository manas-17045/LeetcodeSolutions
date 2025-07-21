# Leetcode 3317: Find the Number of Possible Ways for an Event
# https://leetcode.com/problems/find-the-number-of-possible-ways-for-an-event/
# Solved on 21st of July, 2025
class Solution:
    def numberOfWays(self, n: int, x: int, y: int) -> int:
        """
        Calculates the number of possible ways for an event to occur.
        :param n: The total number of events.
        :param x: The maximum number of successful outcomes.
        :param y: A multiplier for successful outcomes.
        :return: The total number of ways modulo 10^9 + 7.
        """
        mod = 10**9 + 7

        dp = [0] * (x + 1)
        dp[0] = 1

        for i in range(1, n + 1):
            limit = min(i, x)
            for j in range(limit, 0, -1):
                termOne = dp[j] * j
                termTwo = dp[j - 1] * (x - j + 1)
                dp[j] = (termOne + termTwo) % mod
            dp[0] = 0

        totalWays = 0
        powerOfY = 1

        for k in range(1, (x + 1)):
            powerOfY = (powerOfY * y) % mod
            term = (dp[k] * powerOfY) % mod
            totalWays = (totalWays + term) % mod

        return totalWays