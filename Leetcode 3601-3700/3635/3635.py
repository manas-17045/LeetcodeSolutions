# Leetcode 3635: Earliest Finish Time for Land and Water Rides II
# https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-ii/
# Solved on 25th of November, 2025
class Solution:
    def earliestFinishTime(self, landStartTime: list[int], landDuration: list[int], waterStartTime: list[int], waterDuration: list[int]) -> int:
        """
        Calculates the earliest possible finish time for a sequence of two rides,
        one land ride and one water ride, where the order can be either land then water
        or water then land.

        Args:
            landStartTime: A list of start times for available land rides.
            landDuration: A list of durations for available land rides.
            waterStartTime: A list of start times for available water rides.
            waterDuration: A list of durations for available water rides.

        Returns:
            The earliest finish time for completing one land ride and one water ride.
        """
        minLandFinish = min(s + d for s, d in zip(landStartTime, landDuration))
        minWaterFinish = min(s + d for s, d in zip(waterStartTime, waterDuration))

        landToWater = min(max(s, minLandFinish) + d for s, d in zip(waterStartTime, waterDuration))
        waterToLand = min(max(s, minWaterFinish) + d for s, d in zip(landStartTime, landDuration))

        return min(landToWater, waterToLand)