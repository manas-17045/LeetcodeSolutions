# Leetcode 2327: Number of People Aware of a Secret
# https://leetcode.com/problems/number-of-people-aware-of-a-secret/
# Solved on 9th of September, 2025
class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        """
        Calculates the number of people aware of a secret on day 'n'.

        Args:
            n (int): The total number of days.
            delay (int): The number of days a person waits before sharing the secret.
            forget (int): The number of days a person remembers the secret before forgetting.
        Returns:
            int: The number of people aware of the secret on day 'n'.
        """

        mod = 10 ** 9 + 7
        dp = [0] * (n + 1)
        dp[1] = 1
        shareCount = 0

        for i in range(2, n + 1):
            if i - delay > 0:
                shareCount = (shareCount + dp[i - delay]) % mod

            if i - forget > 0:
                shareCount = (shareCount - dp[i - forget] + mod) % mod

            dp[i] = shareCount

        totalAware = 0
        for i in range(n - forget + 1, n + 1):
            totalAware = (totalAware + dp[i]) % mod

        return totalAware