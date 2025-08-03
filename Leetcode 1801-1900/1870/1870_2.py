# Leetcode 1870: Minimum Speed to Arrive on Time
# https://leetcode.com/problems/minimum-speed-to-arrive-on-time/
# Solved on 3rd of August, 2025
import math


class Solution:
    def minSpeedOnTime(self, dist: list[int], hour: float) -> int:
        """
        Calculates the minimum integer speed required to complete all train rides within the given hour.
        :param dist: A list of integers representing the distances of each train ride.
        :param hour: A float representing the maximum total time allowed.
        :return: The minimum integer speed, or -1 if it's impossible to complete all rides within the given hour.
        """
        n = len(dist)
        # If hour <= n - 1, we can't even catch the last train's fractional ride
        if hour <= n - 1:
            return -1
        
        def can_make(speed: int) -> bool:
            # Compute total time at this speed
            t = 0.0
            for d in dist[:-1]:
                t += math.ceil(d / speed)
                # early exit if already too slow
                if t > hour:
                    return False
            t += dist[-1] / speed
            return t <= hour
        
        lo, hi = 1, 10**7
        ans = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if can_make(mid):
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1
        
        return ans