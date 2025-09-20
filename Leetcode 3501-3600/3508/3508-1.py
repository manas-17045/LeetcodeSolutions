# Leetcode 3508: Implement Router
# https://leetcode.com/problems/implement-router/
# Solved on 20th of September, 2025
import bisect
import collections


class Router:

    def __init__(self, memoryLimit: int):
        self.memoryLimit = memoryLimit
        self.packetQueue = collections.deque()
        self.packetSet = set()
        self.packetsByDestination = collections.defaultdict(list)

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        packet = (source, destination, timestamp)
        if packet in self.packetSet:
            return False

        if len(self.packetQueue) == self.memoryLimit:
            oldestPacket = self.packetQueue.popleft()
            self.packetSet.remove(oldestPacket)
            oldSource, oldDestination, oldTimestamp = oldestPacket

            destList = self.packetsByDestination[oldDestination]
            destList.pop(0)

        self.packetQueue.append(packet)
        self.packetSet.add(packet)
        self.packetsByDestination[destination].append((timestamp, source))

        return True

    def forwardPacket(self) -> list[int]:
        if not self.packetQueue:
            return []

        packetToForward = self.packetQueue.popleft()
        self.packetSet.remove(packetToForward)

        source, destination, timestamp = packetToForward
        destList = self.packetsByDestination[destination]
        destList.pop(0)

        return [source, destination, timestamp]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        destList = self.packetsByDestination.get(destination, [])
        if not destList:
            return 0

        startTuple = (startTime, -1)
        endTuple = (endTime, float('inf'))

        startIndex = bisect.bisect_left(destList, startTuple)
        endIndex = bisect.bisect_right(destList, endTuple)

        return endIndex - startIndex