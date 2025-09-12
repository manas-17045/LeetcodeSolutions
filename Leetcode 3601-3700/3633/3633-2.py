# Leetcode 3633: Earliest Finish Time for Land and Water Rides I
# https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-i/
# Solved on 13th of September, 2025
import math


class Solution:
    def earliestFinishTime(self, landStartTime: list[int], landDuration: list[int], waterStartTime: list[int], waterDuration: list[int]) -> int:
        """
        Calculates the earliest possible finish time for a sequence of tasks,
        where tasks are divided into 'land' tasks and 'water' tasks.
        The tasks can be performed in two orders: land tasks then water tasks,
        or water tasks then land tasks.

        Args:
            landStartTime (list[int]): A list of start times for land tasks.
            landDuration (list[int]): A list of durations for land tasks.
            waterStartTime (list[int]): A list of start times for water tasks.
            waterDuration (list[int]): A list of durations for water tasks.

        Returns:
            int: The earliest possible finish time among all possible task sequences.
        """
        n = len(landStartTime)
        m = len(waterStartTime)
        ans = math.inf

        # Try order: land -> water
        for i in range(n):
            land_finish = landStartTime[i] + landDuration[i]
            for j in range(m):
                finish = max(waterStartTime[j], land_finish) + waterDuration[j]
                if finish < ans:
                    ans = finish

        # Try order: water -> land
        for j in range(m):
            water_finish = waterStartTime[j] + waterDuration[j]
            for i in range(n):
                finish = max(landStartTime[i], water_finish) + landDuration[i]
                if finish < ans:
                    ans = finish

        return int(ans)