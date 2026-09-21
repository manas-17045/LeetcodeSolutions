# Leetcode 4027: Elevator Requests III
# https://leetcode.com/problems/elevator-requests-iii/
# Solved on 21st of September, 2026
class Solution:
    def elevatorRequests(self, n: int, start: int, requests: list[list[int]]) -> int:
        """
        Calculates the minimum time needed to fulfill all elevator requests.
        
        Args:
            n (int): The total number of floors in the building.
            start (int): The starting floor of the elevator at time 0.
            requests (list[list[int]]): A list of requests where each request is [arrivalTime, requestedFloor].
            
        Returns:
            int: The minimum time in seconds required to fulfill all requests.
        """
        numRequests = len(requests)
        totalMasks = 1 << numRequests
        minTimeTable = [[float('inf')] * numRequests for _ in range(totalMasks)]

        for i in range(numRequests):
            arrivalTime = requests[i][0]
            targetFloor = requests[i][1]
            travelTime = abs(start - targetFloor)
            minTimeTable[1 << i][i] = max(travelTime, arrivalTime)

        for currentMask in range(totalMasks):
            for lastRequest in range(numRequests):
                if currentMask & (1 << lastRequest):
                    currentTime = minTimeTable[currentMask][lastRequest]

                    if currentTime != float('inf'):
                        currentFloor = requests[lastRequest][1]

                        for nextRequest in range(numRequests):
                            if not (currentMask & (1 << nextRequest)):
                                nextMask = currentMask | (1 << nextRequest)
                                nextArrival = requests[nextRequest][0]
                                nextFloor = requests[nextRequest][1]
                                nextTravelTime = abs(currentFloor - nextFloor)

                                completionTime = max(currentTime + nextTravelTime, nextArrival)

                                if completionTime < minTimeTable[nextMask][nextRequest]:
                                    minTimeTable[nextMask][nextRequest] = completionTime

        finalMask = totalMasks - 1
        
        return int(min(minTimeTable[finalMask]))