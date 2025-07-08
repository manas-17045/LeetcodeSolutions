# Leetcode 1751: Maximum Number of Events That Can Be Attended II
# https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended-ii/
# Solved on 8th of July, 2025
import bisect


class Solution:
    def maxValue(self, events: list[list[int]], k: int) -> int:
        """
        Calculates the maximum total value of events that can be attended,
        given a maximum number of events `k` that can be attended.

        Args:
            events (list[list[int]]): A list of events, where each event is
                                      [startDay, endDay, value].
            k (int): The maximum number of events that can be attended.

        Returns:
            int: The maximum total value of events that can be attended.

        This solution uses dynamic programming with a bottom-up approach.
        """
        numEvents = len(events)
        events.sort()

        startDays = [e[0] for e in events]
        dp = [[0] * (k + 1) for _ in range(numEvents + 1)]

        for i in range((numEvents - 1), -1, -1):
            currentEvent = events[i]
            currentValue = currentEvent[2]
            currentEndDay = currentEvent[1]

            nextI = bisect.bisect_right(startDays, currentEndDay)

            for count in range(1, (k + 1)):
                resSkip = dp[i + 1][count]
                resAttend = currentValue + dp[nextI][count - 1]
                dp[i][count] = max(resSkip, resAttend)

        return dp[0][k]