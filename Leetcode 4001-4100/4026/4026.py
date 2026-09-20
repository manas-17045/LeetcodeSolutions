# Leetcode 4026: Maximum Gap Between Stations
# https://leetcode.com/problems/maximum-gap-between-stations/
# Solved on 20th of Septemeber, 2026
class Solution:
    def maximumGap(self, skill: str, station: str) -> int:
        """
        Calculates the maximum possible gap between stations assigned to
        consecutive workers.

        Parameters:
            skill (str): String where skill[i] represents worker i's required skill.
            station (str): String where station[j] represents station j's supported skill.

        Returns:
            int: The maximum possible gap between adjacent assigned station indices.
        """
        numWorkers = len(skill)
        numStations = len(station)

        if numWorkers <= 1:
            return 0

        earliestPositions = [0] * numWorkers
        workerIndex = 0

        for stationIndex in range(numStations - 1, -1, -1):
            if station[stationIndex] == skill[workerIndex]:
                earliestPositions[workerIndex] = stationIndex
                workerIndex += 1
                if workerIndex == numWorkers:
                    break

        maxGap = 0
        workerIndex = numWorkers - 1

        for stationIndex in range(numStations - 1, -1, -1):
            if station[stationIndex] == skill[workerIndex]:
                if workerIndex > 0:
                    currentGap = stationIndex - earliestPositions[workerIndex - 1]
                    if currentGap > maxGap:
                        maxGap = currentGap
                workerIndex -= 1
                if workerIndex < 1:
                    break

        return maxGap