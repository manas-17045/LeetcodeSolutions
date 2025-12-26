# Leetcode 3733: Minimum Time to Complete All Deliveries
# https://leetcode.com/problems/minimum-time-to-complete-all-deliveries/
# Solved on 26th of December, 2025
import math


class Solution:
    def minimumTime(self, d: list[int], r: list[int]) -> int:
        """
        Calculates the minimum time required to complete all deliveries.

        Args:
            d: A list of two integers representing the number of deliveries for two different types.
            r: A list of two integers representing the recharge times for the two delivery types.
        Returns:
            The minimum time required to complete all deliveries.
        """
        d1 = d[0]
        d2 = d[1]
        r1 = r[0]
        r2 = r[1]

        lcmVal = (r1 * r2) // math.gcd(r1, r2)
        low = 1
        high = 10 ** 15

        ans = high
        while low <= high:
            mid = (low + high) // 2
            recharge1 = mid // r1
            avail1 = mid - recharge1
            recharge2 = mid // r2
            avail2 = mid - recharge2
            commonRecharge = mid // lcmVal
            unionAvail = mid - commonRecharge

            if avail1 >= d1 and avail2 >= d2 and unionAvail >= (d1 + d2):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans