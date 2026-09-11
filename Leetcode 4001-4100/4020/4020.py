# Leetcode 4020: Elevator Requests I
# https://leetcode.com/problems/elevator-requests-i/
# Solved on 11th of September, 2026
class Solution:
    def elevatorRequests(self, n: int, requests: list[int]) -> int:
        """
        Calculate the total time in seconds required to serve all elevator requests.

        Parameters:
            n (int): The total number of floors in the building.
            requests (list[int]): The sequence of floor requests.

        Returns:
            int: The total time required to serve all requests.
        """
        totalTime = 0
        currentFloor = 0

        for targetFloor in requests:
            totalTime += abs(targetFloor - currentFloor)
            currentFloor = targetFloor

        return totalTime