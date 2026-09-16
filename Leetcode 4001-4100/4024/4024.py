# Leetcode 4024: Nearest Available Drone
# https://leetcode.com/problems/nearest-available-drone/
# Solved on 16th of September, 2026
class Solution:
    def nearestDrone(self, drones: list[list[int]], target: list[int]) -> int:
        """
        Finds the index of the nearest reachable drone to the target coordinates.

        Parameters:
            drones (list[list[int]]): A list where each element contains [x, y, range] of a drone.
            target (list[int]): The target coordinates [tx, ty].

        Returns:
            int: The index of the reachable drone with the minimum Manhattan distance,
                 favoring the smallest index on ties, or -1 if no drone can reach the target.
        """
        targetX, targetY = target
        bestIndex = -1
        minDistance = float("inf")

        for droneIndex, (droneX, droneY, droneRange) in enumerate(drones):
            currentDistance = abs(droneX - targetX) + abs(droneY - targetY)
            if currentDistance <= droneRange and currentDistance < minDistance:
                minDistance = currentDistance
                bestIndex = droneIndex
        
        return bestIndex