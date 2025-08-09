# Leetcode 2528: Maximize the Minimum Powered City
# https://leetcode.com/problems/maximize-the-minimum-powered-city/
# Solved on 9th of August, 2025
class Solution:
    def maxPower(self, stations: list[int], r: int, k: int) -> int:
        """
        Calculates the maximum possible minimum power among all cities after adding at most k stations.
        :param stations: A list of integers representing the initial number of stations in each city.
        :param r: An integer representing the range of influence for a station.
        :param k: An integer representing the maximum number of additional stations that can be built.
        :return: An integer representing the maximum possible minimum power.
        """
        n = len(stations)
        # Prefix sum to compute base power for each city quickly
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + stations[i]
        base = [0] * n
        for i in range(n):
            L = max(0, (i - r))
            R = min(n - 1, (i + r))
            base[i] = pref[R + 1] - pref[L]

        # Upper bound: no city can gain more than k extra power
        lo, hi = min(base), max(base) + k
        ans = lo

        def can_make(target: int) -> bool:
            # Difference array to manage added-stations contributions efficiently
            diff = [0] * (n + 1)
            # Current cumulative added contribution at city i
            cur_add = 0
            # Total stations used so far
            used = 0

            for i in range(n):
                cur_add += diff[i]
                cur_power = base[i] + cur_add
                if cur_power < target:
                    need = target - cur_power
                    used += need
                    if used > k:
                        return False
                    # Place these 'need' stations at position pos = min(n-1, i+r)
                    pos = min(n - 1, i + r)
                    # Calculate end index of effect and schedule removal
                    end = min(n - 1, pos + r)
                    cur_add += need
                    diff[end + 1] -= need

            return True
        
        while lo <= hi:
            mid = (lo + hi) // 2
            if can_make(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1

        return ans