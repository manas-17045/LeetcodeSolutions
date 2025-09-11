# Leetcode 3296: Minimum Number of Seconds to Make Mountain Height Zero
# https://leetcode.com/problems/minimum-number-of-seconds-to-make-mountain-array
# Solved on 11th of September, 2025
import math


class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: list[int]) -> int:
        """
        Calculates the minimum number of seconds required to reduce the mountain height to zero.

        Args:
            mountainHeight (int): The initial height of the mountain.
            workerTimes (list[int]): A list of integers representing the time each worker takes to reduce 1 unit of height.

        Returns:
            int: The minimum number of seconds required.
        """

        def canFinish(time: int) -> bool:
            totalHeightReduced = 0
            for singleWorkerTime in workerTimes:
                discriminant = 1 + 8 * time // singleWorkerTime
                heightReduced = (math.isqrt(discriminant) - 1) // 2
                totalHeightReduced += heightReduced
                if totalHeightReduced >= mountainHeight:
                    return True
            return False

        left = 0
        right = 10**24
        ans = right

        while left <= right:
            mid = left + (right - left) // 2
            if canFinish(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans