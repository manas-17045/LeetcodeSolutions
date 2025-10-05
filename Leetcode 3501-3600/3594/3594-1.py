# Leetcode 3594: Minimum Time to Transport All Individuals
# https://leetcode.com/problems/minimum-time-to-transport-all-individuals/
# Solved on 5th of October, 2025
import heapq
import itertools


class Solution:
    def minTime(self, n: int, k: int, m:int, time: list[int], mul: list[float]) -> float:
        """
        Calculates the minimum time required to transport all individuals from the starting bank to the destination bank.

        Args:
            n (int): The total number of individuals.
            k (int): The maximum capacity of the boat.
            m (int): The number of stages for the time multiplier.
            time (list[int]): A list where time[i] is the time required for individual i to cross the river alone.
            mul (list[float]): A list where mul[j] is the multiplier for the j-th stage.

        Returns:
            float: The minimum time to transport all individuals. Returns -1.0 if it's not possible
                   (though the problem constraints usually guarantee a solution).
        """
        minDistances = {}
        initialMask = (1 << n) - 1
        priorityQueue = [(0.0, initialMask, 0, 0)]
        minDistances[(initialMask, 0, 0)] = 0.0

        while priorityQueue:
            currentTime, currentMask, currentStage, boatLocation = heapq.heappop(priorityQueue)

            if currentTime > minDistances.get((currentMask, currentStage, boatLocation), float('inf')):
                continue

            if currentMask == 0:
                return currentTime

            if boatLocation == 0:
                peopleAtStartIndices = []
                for i in range(n):
                    if (currentMask >> i) & 1:
                        peopleAtStartIndices.append(i)

                numPeopleAtStart = len(peopleAtStartIndices)
                for groupSize in range(1, min(k, numPeopleAtStart) + 1):
                    for groupIndices in itertools.combinations(peopleAtStartIndices, groupSize):
                        maxStrength = 0
                        groupMask = 0
                        for personIndex in groupIndices:
                            maxStrength = max(maxStrength, time[personIndex])
                            groupMask |= (1 << personIndex)

                        forwardTime = maxStrength * mul[currentStage]
                        newTime = currentTime + forwardTime
                        newMask = currentMask ^ groupMask
                        newStage = (currentStage + int(forwardTime)) % m
                        newBoatLocation = 1

                        if newTime < minDistances.get((newMask, newStage, newBoatLocation), float('inf')):
                            minDistances[(newMask, newStage, newBoatLocation)] = newTime
                            heapq.heappush(priorityQueue, (newTime, newMask, newStage, newBoatLocation))

            else:
                for returnerIndex in range(n):
                    if not ((currentMask >> returnerIndex) & 1):
                        returnTime = time[returnerIndex] * mul[currentStage]
                        newTime = currentTime + returnTime

                        newMask = currentMask | (1 << returnerIndex)
                        newStage = (currentStage + int(returnTime)) % m
                        newBoatLocation = 0

                        if newTime < minDistances.get((newMask, newStage, newBoatLocation), float('inf')):
                            minDistances[(newMask, newStage, newBoatLocation)] = newTime
                            heapq.heappush(priorityQueue, (newTime, newMask, newStage, newBoatLocation))


        return -1.0