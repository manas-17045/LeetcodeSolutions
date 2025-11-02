# Leetcode 2054: Two Best Non-Overlapping Events
# https://leetcode.com/problems/two-best-non-overlapping-events/
# Solved on 2nd of November, 2025
import heapq


class Solution:
    def maxTwoEvents(self, events: list[list[int]]) -> int:
        """
        Calculates the maximum total value of two non-overlapping events.

        Args:
            events: A list of events, where each event is [start_time, end_time, value].
        Returns:
            The maximum total value of two non-overlapping events.
        """
        events.sort()

        minHeap = []
        maxResult = 0
        maxPrefixValue = 0

        for start, end, value in events:
            while minHeap and minHeap[0][0] < start:
                endedTime, endedValue = heapq.heappop(minHeap)
                maxPrefixValue = max(maxPrefixValue, endedValue)

            maxResult = max(maxResult, value)
            maxResult = max(maxResult, value + maxPrefixValue)

            heapq.heappush(minHeap, (end, value))

        return maxResult