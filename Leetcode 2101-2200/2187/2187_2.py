# Leetcode 2187: Minimum Time to Complete Trips
# https://leetcode.com/problems/minimum-time-to-complete-trips/
# Solved on 3rd of August, 2025
class Solution:
    def minimumTime(self, time: list[int], totalTrips: int) -> int:
        """
        Calculates the minimum time required for all buses to complete a given total number of trips.

        Args:
            time (list[int]): A list where time[i] is the time taken by the i-th bus to complete one trip.
            totalTrips (int): The total number of trips that need to be completed.

        Returns:
            int: The minimum time required to complete totalTrips.
        """
        # The fastest possible time for one trip
        min_time = min(time)
        left, right = 1, min_time * totalTrips
        ans = right

        while left <= right:
            mid = (left + right) // 2
            # Count how many trips can be done in 'mid' time
            trips = 0
            for t in time:
                trips += mid // t
                # Early exit once we've reached the goal
                if trips >= totalTrips:
                    break

            if trips >= totalTrips:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans