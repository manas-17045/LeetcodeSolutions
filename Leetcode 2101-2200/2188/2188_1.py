# Leetcode 2188: Minimum Time to Finish the Race
# https://leetcode.com/problems/minimum-time-to-finish-the-race/
# Solved on 10th of July, 2025
import math


class Solution:
    def minimumFinishTime(self, tires: list[list[int]], changeTime: int, numLaps: int) -> int:
        """
        Calculates the minimum time to finish a race of `numLaps` laps.

        Args:
            tires: A list of lists, where each inner list `[f, r]` represents a tire type.
                   `f` is the time taken for the first lap with this tire, and `r` is
                   the factor by which the lap time increases for subsequent laps.
            changeTime: The time taken to change tires.
            numLaps: The total number of laps to complete.

        Returns:
            The minimum total time required to finish the race.

        This solution uses dynamic programming.
        """
        noChangeCost = [math.inf] * (numLaps + 1)

        for f, r in tires:
            currentLapTime = f
            stintTime = 0
            lapsInStint = 0

            while True:
                stintTime += currentLapTime
                lapsInStint += 1
                if lapsInStint > numLaps:
                    break

                noChangeCost[lapsInStint] = min(noChangeCost[lapsInStint], stintTime)

                if (currentLapTime * r) > (changeTime + f):
                    break

                currentLapTime *= r

        minTime = [math.inf] * (numLaps + 1)
        minTime[0] = -changeTime

        for i in range(1, numLaps + 1):
            for j in range(i, (i + 1)):
                if noChangeCost[j] != math.inf:
                    lapsDone = i - j
                    newTotalTime = minTime[lapsDone] + changeTime + noChangeCost[j]
                    minTime[i] = min(minTime[i], newTotalTime)

        return int(minTime[numLaps])