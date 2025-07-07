# Leetcode 1353: Maximum Number of Events That Can be Attended
# https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/
# Solved on 7th of July, 2025
import heapq


class Solution:
    def maxEvents(self, events: list[list[int]]) -> int:
        """
        Given an array of events where events[i] = [startDayi, endDayi],
        return the maximum number of events you can attend.

        You can only attend one event at a time.
        The event must be attended on some day d where startDayi <= d <= endDayi.

        Args:
            events: A list of lists, where each inner list represents an event [startDay, endDay].
        Returns:
            The maximum number of events that can be attended.
        """
        events.sort()

        totalEvents = len(events)
        eventIndex = 0
        attendedEvents = 0

        minHeap = []

        currentDay = 0

        while eventIndex < totalEvents or minHeap:
            if not minHeap:
                currentDay = events[eventIndex][0]

            while (eventIndex < totalEvents) and (events[eventIndex][0] <= currentDay):
                heapq.heappush(minHeap, events[eventIndex][1])
                eventIndex += 1

            while minHeap and minHeap[0] < currentDay:
                heapq.heappop(minHeap)

            if minHeap:
                heapq.heappop(minHeap)
                attendedEvents += 1

            currentDay += 1

        return attendedEvents