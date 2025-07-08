# Leetcode 1751: Maximum Number of Events That Can Be Attended II
# https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended-ii/
# Solved on 8th of July, 2025
import bisect
import sys
from functools import lru_cache


class Solution:
    def maxValue(self, events: list[list[int]], k: int) -> int:
        """
        Calculates the maximum total value of events that can be attended, given a maximum number of events `k`.

        Args:
            events: A list of events, where each event is represented as [start_day, end_day, value].
            k: The maximum number of events that can be attended.

        Returns:
            The maximum total value of events that can be attended.
        """
        sys.setrecursionlimit(10**7)
        # Sort by start day
        events.sort(key=lambda x: x[0])
        starts = [e[0] for e in events]
        ends = [e[1] for e in events]
        vals = [e[2] for e in events]
        n = len(events)

        # For each event i, find the first event j > i with start[j] > end[i]
        next_idx = [0] * n
        for i in range(n):
            next_idx[i] = bisect.bisect_right(starts, ends[i])

        @lru_cache(None)
        def f(i: int, rem: int) -> int:
            if i >= n or rem == 0:
                return 0

            best = f((i + 1), rem)

            j = next_idx[i]
            best = max(best, (vals[i] + f(j, (rem - 1))))
            return best

        return f(0, k)