# Leetcode 3633: Earliest Finish Time for Land and Water Rides I
# https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-i/
# Solved on 13th of September, 2025
class Solution:
    def earliestFinishTime(self, landStartTime: list[int], landDuration: list[int], waterStartTime: list[int], waterDuration: list[int]) -> int:
        """
        Calculates the earliest possible finish time for completing one land ride and one water ride.

        Args:
            landStartTime: A list of integers representing the start times of available land rides.
            landDuration: A list of integers representing the durations of available land rides.
            waterStartTime: A list of integers representing the start times of available water rides.
            waterDuration: A list of integers representing the durations of available water rides.
        Returns:
            An integer representing the earliest finish time for completing one land and one water ride.
        """
        numLandRides = len(landStartTime)
        numWaterRides = len(waterStartTime)

        earliestTime = float('inf')

        for i in range(numLandRides):
            for j in range(numWaterRides):

                # Path 1: Land ride i -> Water ride j
                landFinishTime = landStartTime[i] + landDuration[i]
                waterStartTimeAfterLand = max(landFinishTime, waterStartTime[j])
                path1FinishTime = waterStartTimeAfterLand + waterDuration[j]

                # Path 2: Water ride j -> Land ride i
                waterFinishTime = waterStartTime[j] + waterDuration[j]
                landStartTimeAfterWater = max(waterFinishTime, landStartTime[i])
                path2FinishTime = landStartTimeAfterWater + landDuration[i]

                earliestTime = min(earliestTime, path1FinishTime, path2FinishTime)

        return earliestTime