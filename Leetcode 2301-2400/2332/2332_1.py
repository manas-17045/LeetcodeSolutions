# Leetcode 2332: The Latest Time to Catch a Bus
# https://leetcode.com/problems/the-latest-time-to-catch-a-bus/
# Solved on 2nd of August, 2025
class Solution:
    def latestTimeCatchTheBus(self, buses: list[int], passengers: list[int], capacity: int) -> int:
        """
        Finds the latest possible time a new passenger can arrive at a bus stop
        and still catch a bus, given bus schedules, passenger arrival times, and bus capacities.
        :param buses: A list of integers representing the departure times of buses.
        :param passengers: A list of integers representing the arrival times of passengers.
        :param capacity: An integer representing the maximum number of passengers a bus can hold.
        :return: An integer representing the latest possible arrival time for a new passenger.
        """
        buses.sort()
        passengers.sort()

        passengerIndex = 0
        passengersOnLastBus = 0

        for busTime in buses:
            passengersBoardedThisBus = 0
            while (passengerIndex < len(passengers) and
                   passengers[passengerIndex] <= busTime and
                   passengersOnLastBus < capacity):
                passengersBoardedThisBus += 1
                passengerIndex += 1
            passengersOnLastBus = passengersBoardedThisBus

        latestTime = 0
        if passengersOnLastBus < capacity:
            latestTime = buses[-1]
        else:
            latestTime = passengers[passengerIndex - 1]

        passengerSet = set(passengers)
        while latestTime in passengerSet:
            latestTime -= 1

        return latestTime