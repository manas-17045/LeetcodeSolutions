# Leetcode 3296: Minimum Number of Seconds to Make Mountain Height Zero
# https://leetcode.com/problems/minimum-number-of-seconds-to-make-mountain-array
# Solved on 11th of September, 2025
import math


class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: list[int]) -> int:
        """
        Calculates the minimum number of seconds required to reduce a mountain of given height to 0.

        Args:
            mountainHeight (int): The initial height of the mountain.
            workerTimes (list[int]): A list of integers where each element represents the time a worker takes to remove 1 unit of height.
        Returns:
            int: The minimum number of seconds required.
        """
        # helper: can we reduce the mountain to 0 within time t?
        def can(t: int) -> bool:
            total = 0
            for w in workerTimes:
                # number of units this worker can reduce, k, satisfies:
                # w * k * (k+1) / 2 <= t  ->  k*(k+1)/2 <= t // w
                limit = t // w
                if limit <= 0:
                    continue
                # solve k*(k+1) <= 2*limit  using integer sqrt:
                # discriminant for k = (-1 + sqrt(1 + 8*limit)) / 2
                D = 1 + 8 * limit
                k = (math.isqrt(D) - 1) // 2
                total += k
                if total >= mountainHeight:
                    return True
            return False

        # binary search bounds
        min_w = min(workerTimes)
        # upper bound: single fastest worker removes all height alone
        hi = min_w * mountainHeight * (mountainHeight + 1) // 2
        lo = 0

        while lo < hi:
            mid = (lo + hi) // 2
            if can(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo