# Leetcode 1883: Minimum Skips to Arrive at Meeting On Time
# https://leetcode.com/problems/minimum-skips-to-arrive-at-meeting-on-time/
# Solved on 10th of July, 2025
class Solution:
    def minSkips(self, dist: list[int], speed: int, hoursBefore: int) -> int:
        """
        Calculates the minimum number of skips required to arrive at a meeting on time.

        Args:
            dist (list[int]): A list of integers representing the distances of roads.
            speed (int): An integer representing the speed of travel.
            hoursBefore (int): An integer representing the maximum hours allowed before the meeting.

        Returns:
            int: The minimum number of skips required.
                 Returns -1 if it's impossible to arrive on time even with all skips.

        This function uses dynamic programming to find the minimum skips.
        """
        numRoads = len(dist)
        maxTimeScaled = hoursBefore * speed

        totalDist = sum(dist)

        if totalDist > maxTimeScaled:
            return -1

        infinity = float('inf')
        dp = [infinity] * numRoads

        dp[0] = dist[0]

        for i in range(1, numRoads):
            distI = dist[i]

            for j in range(i, -1, -1):
                timeNoSkip = infinity
                if dp[j] != infinity:
                    restedTime = ((dp[j] + speed - 1) // speed) * speed
                    timeNoSkip = dp[j] + restedTime + distI

                timeSkip = infinity
                if (j > 0) and (dp[j - 1] != infinity):
                    timeSkip = dp[j - 1] + distI

                dp[j] = min(timeNoSkip, timeSkip)

        for k in range(numRoads):
            if dp[k] <= maxTimeScaled:
                return k

        return -1