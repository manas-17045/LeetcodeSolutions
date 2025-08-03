# Leetcode 1870: Minimum Speed to Arrive on Time
# https://leetcode.com/problems/minimum-speed-to-arrive-on-time/
# Solved on 3rd of August, 2025
class Solution:
    def minSpeedOnTime(self, dist: list[int], hour: float) -> int:
        """
        Calculates the minimum integer speed required to arrive on time.

        Args:
            dist (list[int]): A list of distances to be covered.
            hour (float): The maximum allowed time to cover all distances.
        Returns:
            int: The minimum integer speed required, or -1 if it's impossible to arrive on time.
        """
        n = len(dist)

        if hour <= float(n - 1):
            return -1

        left = 1
        right = 10**7
        minSpeed = -1

        while left <= right:
            speed = (left + right) // 2

            totalTime = 0.0
            for i in range(n - 1):
                totalTime += (dist[i] + speed - 1) // speed

            totalTime += dist[n - 1] / speed

            if totalTime <= hour:
                minSpeed = speed
                right = speed - 1
            else:
                left = speed + 1

        return minSpeed