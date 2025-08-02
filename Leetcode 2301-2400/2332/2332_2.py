# Leetcode 2332: The Latest Time to Catch a Bus
# https://leetcode.com/problems/the-latest-time-to-catch-a-bus/
# Solved on 2nd of August, 2025
class Solution:
    def latestTimeCatchTheBus(self, buses: list[int], passengers: list[int], capacity: int) -> int:
        """
        Finds the latest possible time a new passenger can arrive at the bus station
        to catch a bus, given bus schedules and existing passenger arrival times.

        Args:
            buses (list[int]): A list of integers representing the departure times of buses.
            passengers (list[int]): A list of integers representing the arrival times of existing passengers.
            capacity (int): The maximum number of passengers each bus can hold.
        Returns:
            int: The latest possible arrival time for a new passenger.
        """
        # Sort the buses and passenger arrivals
        buses.sort()
        passengers.sort()
        passenger_set = set(passengers)

        # Pointer into passenger
        i = 0
        m = len(passengers)
        # Best (max) arrival time found
        best = 0

        for bus_time in buses:
            # Count how many passengers can board this bus
            # and record the last one boarded
            start = i
            # Move i forward over all passengers who arrive <= bus_time
            while i <= m and passengers[i] <= bus_time and i - start < capacity:
                i += 1
            boarded = i - start

            if boarded < capacity:
                # There's at least one empty seat -> could arrive at bus_time
                candidate = bus_time
            else:
                # Bus is full 0> must arrive just before the last boarded passenger
                # Last boarded passenger is passengers[i - 1]
                candidate = passengers[i - 1] - 1

            # Bump candidate down if it collides with another passenger
            while candidate in passenger_set:
                candidate -= 1

            best = max(best, candidate)

        return best