# Leetcode 4023: Elevator Requests II
# https://leetcode.com/problems/elevator-requests-ii/
# Solved on 14th of September, 2026
class Solution:
    def elevatorRequests(self, n: int, start: int, requests: list[int]) -> int:
        """
        Calculates the minimum total penalty required to fulfill all elevator requests.

        Parameters:
            n (int): The total number of floors in the building.
            start (int): The starting floor of the elevator.
            requests (list[int]): A list of requested floors.

        Returns:
            int: The minimum total penalty.
        """
        reqSet = set(requests)
        floors = list(reqSet)

        if start not in reqSet:
            floors.append(start)
            
        floors.sort()

        totalReqs = len(requests)
        numFloors = len(floors)
        startIndex = floors.index(start)

        prefixReqs = [0] * (numFloors + 1)
        for i in range(numFloors):
            prefixReqs[i + 1] = prefixReqs[i] + (1 if floors[i] in reqSet else 0)

        currDp = [[0, 0]]

        for length in range(numFloors - 1, 0, -1):
            nextDp = [[float('inf'), float('inf')] for _ in range(numFloors - length + 1)]

            for i in range(numFloors - length + 1):
                j = i + length - 1
                remReqs = totalReqs - (prefixReqs[j + 1] - prefixReqs[i])

                ans0 = float('inf')
                ans1 = float('inf')

                if i > 0:
                    leftDp = currDp[i - 1]
                    ans0 = min(ans0, leftDp[0] + (floors[i - 1]) * remReqs)
                    ans1 = min(ans1, leftDp[0] + (floors[j] - floors[i - 1]) * remReqs)

                if j < numFloors - 1:
                    rightDp = currDp[i]
                    ans0 = min(ans0, rightDp[1] + (floors[j + 1] - floors[i]) * remReqs)
                    ans1 = min(ans1, rightDp[1] + (floors[j + 1] - floors[j]) * remReqs)

                nextDp[i][0] = ans0
                nextDp[i][1] = ans1

            currDp = nextDp

        return int(currDp[startIndex][0])