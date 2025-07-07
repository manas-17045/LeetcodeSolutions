# Leetcode 1353: Maximum Number of Events That Can be Attended
# https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/
# Solved on 7th of July, 2025
import heapq


class Solution:
    def maxEvents(self, events: list[list[int]]) -> int:
        """
        Calculates the maximum number of events that can be attended.

        An event can be attended if it is attended on any day between its start day
        and end day (inclusive). Only one event can be attended per day.

        The approach uses a greedy strategy:
        1. Sort events by their start day.
        2. Iterate through days, maintaining a min-heap of available events (by their end day).
        3. On each day, add all events that start on or before the current day to the heap.
        4. Remove events from the heap that have already ended.
        5. If there are available events, attend the one that ends earliest to free up the day
           for future events.
        """
        # Sort events by start day
        events.sort(key=lambda x: x[0])
        min_heap = []   # will store end days of all events available to attend
        i = 0
        n = len(events)
        day = 0
        attended = 0

        # process until we've considered all events and finished attending
        while i < n or min_heap:
            # If no events are available today, fast-forward to the next event's start
            if not min_heap:
                day = max(day, events[i][0])

            # Push all events that start on or before `day` into the heap
            while i < n and events[i][0] <= day:
                heapq.heappush(min_heap, events[i][1])
                i += 1

            # Remove any events that have already ended (< day)
            while min_heap and min_heap[0] < day:
                heapq.heappop(min_heap)

            # Attend the event that ends at the earliest
            if min_heap:
                heapq.heappop(min_heap)
                attended += 1
                day += 1

        return attended