# Leetcode 2402: Meeting Rooms III
# https://leetcode.com/problems/meeting-rooms-iii/
# Solved on 5th of July, 2025
import heapq


class Solution:
    def mostBooked(self, n: int, meetings: list[list[int]]) -> int:
        """
        Calculates the room that hosted the most meetings.

        Args:
            n: The total number of available meeting rooms.
            meetings: A list of meeting time intervals, where each interval is [start, end].

        Returns:
            The index of the room that hosted the most meetings. If there's a tie, the room with the smallest index is returned.
        """
        meetings.sort()

        available = list(range(n))
        heapq.heapify(available)

        used = []
        counts = [0] * n

        for start, end in meetings:
            while used and used[0][0] <= start:
                _, room = heapq.heappop(used)
                heapq.heappush(available, room)

            if not available:
                freeTime, room = heapq.heappop(used)
                end = freeTime + (end - start)
            else:
                room = heapq.heappop(available)

            heapq.heappush(used, (end, room))
            counts[room] += 1

        return counts.index(max(counts))