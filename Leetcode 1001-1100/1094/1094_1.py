# Leetcode 1094: Car Pooling
# https://leetcode.com/problems/car-pooling/
# Solved on 19th of August, 2025
class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        """
        Determines if it's possible to carpool all given trips without exceeding the car's capacity.

        Args:
            trips (list[list[int]]): A list of trips, where each trip is [numPassengers, startLocation, endLocation].
            capacity (int): The maximum number of passengers the car can hold.

        Returns:
            bool: True if all trips can be completed within capacity, False otherwise.
        """
        locationChanges = [0] * 1001

        for trip in trips:
            numPassengers = trip[0]
            startLocation = trip[1]
            endLocation = trip[2]

            locationChanges[startLocation] += numPassengers
            locationChanges[endLocation] -= numPassengers

        currentPassengers = 0
        for change in locationChanges:
            currentPassengers += change
            if currentPassengers > capacity:
                return False

        return True