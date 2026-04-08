# Leetcode 3885: Design Event Manager
# https://leetcode.com/problems/design-event-manager/
# Solved on 8th of April, 2026
import heapq


class EventManager:

    def __init__(self, events: list[list[int]]):
        self.eventMap = {}
        self.eventHeap = []
        for eventId, priority in events:
            self.eventMap[eventId] = priority
            heapq.heappush(self.eventHeap, (-priority, eventId))

    def updatePriority(self, eventId: int, newPriority: int) -> None:
        self.eventMap[eventId] = newPriority
        heapq.heappush(self.eventHeap, (-newPriority, eventId))

    def pollHighest(self) -> int:
        while self.eventHeap:
            negPriority, eventId = heapq.heappop(self.eventHeap)
            if eventId in self.eventMap and self.eventMap[eventId] == -negPriority:
                del self.eventMap[eventId]
                return eventId

        return -1