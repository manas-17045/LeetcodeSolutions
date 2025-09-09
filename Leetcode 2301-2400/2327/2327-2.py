# Leetcode 2327: Number of People Aware of a Secret
# https://leetcode.com/problems/number-of-people-aware-of-a-secret/
# Solved on 9th of September, 2025
class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        """
        Calculates the number of people who are aware of a secret on day 'n'.

        Args:
            n (int): The total number of days.
            delay (int): The number of days a person takes to start sharing the secret after learning it.
            forget (int): The number of days a person remembers the secret before forgetting it.
        Returns:
            int: The number of people aware of the secret on day 'n'.
        """
        MOD = 10 ** 9 + 7
        dp = [0] * (n + 1)
        pref = [0] * (n + 1)
        dp[1] = 1
        pref[1] = 1

        for i in range(2, n + 1):
            left = max(1, i - forget + 1)
            right = i - delay
            if right >= left:
                dp[i] = (pref[right] - pref[left - 1]) % MOD
            else:
                dp[i] = 0
            pref[i] = (pref[i - 1] + dp[i]) % MOD

        start = max(0, n - forget)
        result = (pref[n] - pref[start]) % MOD
        return result