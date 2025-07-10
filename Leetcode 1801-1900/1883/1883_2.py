# Leetcode 1883: Minimum Skips to Arrive at Meeting On Time
# https://leetcode.com/problems/minimum-skips-to-arrive-at-meeting-on-time/
# Solved on 10th of July, 2025
class Solution:
    def minSkips(self, dist: list[int], speed: int, hoursBefore: int) -> int:
        """
        Calculates the minimum number of skips required to complete all distances within a given time.

        Args:
            dist (list[int]): A list of distances to travel.
            speed (int): The speed at which to travel.
            hoursBefore (int): The maximum time allowed (in hours).

        Returns:
            int: The minimum number of skips required. Returns -1 if it's not possible
                 to complete all distances within the given time.

        This solution uses dynamic programming. dp[k] stores the minimum total distance traveled
        (scaled by speed) to complete the current segment with 'k' skips.
        """
        n = len(dist)
        INF = 10**30
        target = hoursBefore * speed

        dp = [INF] * (n + 1)
        dp[0] = 0

        for d in dist:
            new_dp = [INF] * (n + 1)
            for k in range(n + 1):
                t0 = dp[k]
                if t0 == INF:
                    continue

                if (k + 1) <= n:
                    new_dp[k + 1] = min(new_dp[k + 1], t0 + d)

                t1 = t0 + d

                w = ((t1 + speed - 1) // speed) * speed
                new_dp[k] = min(new_dp[k], w)
            dp = new_dp

        for k in range(n + 1):
            if dp[k] <= target:
                return k

        return -1