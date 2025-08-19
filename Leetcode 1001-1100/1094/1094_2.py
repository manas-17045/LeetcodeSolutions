# Leetcode 1094: Car Pooling
# https://leetcode.com/problems/car-pooling/
# Solved on 19th of August, 2025
class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        """
        Determines if a car has enough capacity to handle all given trips.
        :param trips: A list of trips, where each trip is [num_passengers, start_location, end_location].
        :param capacity: The maximum number of passengers the car can hold.
        :return: True if the car can handle all trips, False otherwise.
        """
        #  Build events: (location, change_in_passengers)
        events = []
        for num, frm, to in trips:
            # Pick up num at frm
            events.append((frm, num))
            # Drop off num at to
            events.append((to, -num))

        # Sort by location; for same location, process drops (negative) before picks (positive)
        events.sort(key=lambda x: (x[0], x[1]))

        curr = 0
        for _, delta in events:
            curr += delta
            if curr > capacity:
                return False

        return True