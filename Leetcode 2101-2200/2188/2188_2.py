# Leetcode 2188: Minimum Time to Finish the Race
# https://leetcode.com/problems/minimum-time-to-finish-the-race/
# Solved on 10th of July, 2025
import math


class Solution:
    def minimumFinishTime(self, tires: list[list[int]], changeTime: int, numLaps: int) -> int:
        """
        Calculates the minimum time to finish a race of `numLaps` laps, given different tire options
        and a `changeTime` for switching tires.

        Args:
            tires: A list of tire options, where each option `[f, r]` represents a tire
                   with `f` as the time for the first lap and `r` as the multiplier
                   for subsequent laps (time for lap `k` is `f * r^(k-1)`).
            changeTime: The time taken to change tires.
            numLaps: The total number of laps to complete.

        Returns:
            The minimum total time to complete `numLaps`.
        """
        INF = math.inf
        best = [INF] * (numLaps + 1)

        for f, r in tires:
            t = f
            total = 0
            k = 0

            while k < numLaps and (t <= (f + changeTime)):
                k += 1
                total += t
                # Record best for k laps
                if total < best[k]:
                    best[k] = total
                # Prepare next lap time
                t *= r

        dp = [INF] * (numLaps + 1)
        dp[0] = -changeTime

        for i in range(1, (numLaps + 1)):
            for j in range(1, (i + 1)):
                if best[j] < INF:
                    dp[i] = min(dp[i], dp[i - j] + changeTime + best[j])

        return int(dp[numLaps])