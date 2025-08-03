# Leetcode 2187: Minimum Time to Complete Trips
# https://leetcode.com/problems/minimum-time-to-complete-trips/
# Solved on 3rd of August, 2025
class Solution:
    def minimumTime(self, time: list[int], totalTrips: int) -> int:
        """
        Calculates the minimum time required to complete a given number of total trips.

        Args:
            time (list[int]): A list where each element `time[i]` represents the time it takes for the i-th bus to complete one trip.
            totalTrips (int): The total number of trips that need to be completed.

        Returns:
            int: The minimum time required to complete `totalTrips`.
        """
        leftTime = 1
        rightTime = min(time) * totalTrips

        while leftTime < rightTime:
            midTime = leftTime + (rightTime - leftTime) // 2

            tripsDone = 0
            for tripDuration in time:
                tripsDone += midTime // tripDuration

            if tripsDone >= totalTrips:
                rightTime = midTime
            else:
                leftTime = midTime + 1

        return leftTime