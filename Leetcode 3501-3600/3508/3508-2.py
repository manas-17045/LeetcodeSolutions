# Leetcode 3508: Implement Router
# https://leetcode.com/problems/implement-router/
# Solved on 20th of September, 2025
from bisect import bisect_left, bisect_right
from collections import deque, defaultdict


class Router:
    def __init__(self, memoryLimit: int):
        self.memoryLimit = memoryLimit
        self.queue = deque()
        self.seen = set()

        self.dest_to_times = defaultdict(list)
        self.dest_to_offset = defaultdict(int)

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        # Duplicate check first
        key = (source, destination, timestamp)
        if key in self.seen:
            return False

        # if adding would exceed memory limit, remove oldest packets until there's space
        while len(self.queue) >= self.memoryLimit:
            self.remove_oldest()

        # Add the new packet
        self.queue.append((source, destination, timestamp))
        self.seen.add(key)

        # Append timestamp to the per-destination timestamp list (non-decreasing order guaranteed).
        self.dest_to_times[destination].append(timestamp)
        return True

    def forwardPacket(self) -> list[int]:
        if not self.queue:
            return []

        s, d, t = self.queue.popleft()
        self.seen.remove((s, d, t))
        # Logically remove from per-destination timestamps
        self.dest_to_offset[d] += 1

        # Compact if needed (same logic as in remove_oldest)
        lst = self.dest_to_times[d]
        off = self.dest_to_times[d]
        if off == len(lst):
            self.dest_to_times[d] = []
            self.dest_to_offset[d] = 0
        else:
            if off > 256 and off > (len(lst) // 2):
                self.dest_to_times[d] = lst[off:]
                self.dest_to_offset[d] = 0

        return [s, d, t]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        lst = self.dest_to_times.get(destination)
        if not lst:
            return 0
        off = self.dest_to_offset[destination]
        # Binary search within lst[off:]
        lo = bisect_left(lst, startTime, lo=off)
        hi = bisect_right(lst, endTime, lo=off)

        return hi - lo

    def remove_oldest(self) -> None:
        s, d, t = self.queue.popleft()
        self.seen.remove((s, d, t))
        # Logically remove the earliest timestamp for destination d
        self.dest_to_offset[d] += 1

        # Compact the per-destination list if we've consumed it fully or many prefix items
        lst = self.dest_to_times[d]
        off = self.dest_to_offset[d]
        if off == len(lst):
            # Fully consumed, reset to avoid growth
            self.dest_to_times[d] = []
            self.dest_to_offset[d] = 0
        else:
            # Compact if offset becomes large relative to list to keep memory small.
            if off > 256 and off > (len(lst) // 2):
                self.dest_to_times[d] = lst[off:]
                self.dest_to_offset[d] = 0