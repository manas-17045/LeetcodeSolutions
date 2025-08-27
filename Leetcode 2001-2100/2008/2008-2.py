# Leetcode 2008: Maximum Earnings From Taxi
# https://leetcode.com/problems/maximum-earnings-from-taxi/
# Solved on 27th of August, 2025
from bisect import bisect_right


class Solution:
    def maxTaxiEarnings(self, n: int, rides: list[list[int]]) -> int:
        """
        Calculates the maximum earnings from a list of taxi rides.

        Args:
            n (int): The number of cities (not directly used in this solution but part of problem statement).
            rides (list[list[int]]): A list of rides, where each ride is [start_time, end_time, tip].
        Returns:
            int: The maximum total earnings possible.
        """
        # Sort rides by end time
        rides.sort(key=lambda r: r[1])
        ends = [r[1] for r in rides]
        m = len(rides)
        if m == 0:
            return 0

        dp = [0] * m
        for i, (start, end, tip) in enumerate(rides):
            profit = end - start + tip
            # Find last ride that ends <= start (non-overlapping)
            j = bisect_right(ends, start) - 1
            incl = profit + (dp[j] if j >= 0 else 0)
            excl = dp[i-1] if i > 0 else 0
            dp[i] = max(incl, excl)

        return dp[-1]