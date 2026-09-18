# Leetcode 4025: Minimize the Maximum Waiting Time at Synchronized Traffic Lights
# https://leetcode.com/problems/minimize-the-maximum-waiting-time-at-synchronized-traffic-lights/
# Solved on 17th of September, 2026
class Solution:
    def minPenalty(self, period: int, lights: list[int], arrivalTime: list[int]) -> int:
        """
        Calculates the minimum possible maximum waiting time across all cars.

        Parameters:
            period (int): The duration of a full traffic light cycle in seconds.
            lights (list[int]): The duration of the green light phase for each light.
            arrivalTime (list[int]): The arrival time in seconds for each car.

        Returns:
            int: The minimum achievable maximum waiting time among all cars.
        """
        maxGreen = max(lights)
        minPossiblePenalty = 0

        for currentArrival in arrivalTime:
            cycleOffset = currentArrival % period
            if cycleOffset >= maxGreen:
                currentWait = period - cycleOffset
                if currentWait > minPossiblePenalty:
                    minPossiblePenalty = currentWait
            
        return minPossiblePenalty