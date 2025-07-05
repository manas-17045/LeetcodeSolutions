import heapq


class Solution:
    def mostBooked(self, n: int, meetings: list[list[int]]) -> int:
        """
        Determines the room that hosts the most meetings.

        Meetings are assigned to the lowest-numbered available room. If no rooms are available,
        the meeting is delayed until the earliest busy room becomes free, and then assigned
        to that room. The duration of the meeting remains the same.

        Args:
            n: The total number of rooms, indexed from 0 to n-1.
            meetings: A list of meetings, where each meeting is represented as [start_time, end_time].
                      All times are non-negative integers.

        Returns:
            The index of the room that hosted the most meetings. In case of a tie, the room with the smallest index is returned.
        """
        # Sort meetings by start time
        meetings.sort()
        # Min-heap of available rooms (by room number)
        available = list(range(n))
        heapq.heapify(available)
        # Min-heap of busy rooms as (end_time, room_number)
        busy = []
        # Count of meetings held in each room
        count = [0] * n

        for start, end in meetings:
            # Free up rooms that have finished by current star time
            while busy and busy[0][0] <= start:
                freed_end, room = heapq.heappop(busy)
                heapq.heappush(available, room)

            duration = end - start
            if available:
                # Assign lowest-numbered free room
                room = heapq.heappop(available)
                actual_start = start
                actual_end = start + duration
            else:
                # All rooms busy: wait for the earliest to free
                freed_end, room = heapq.heappop(busy)
                actual_start = freed_end
                actual_end = freed_end + duration

            # Record booking
            count[room] += 1
            # Mark room as busy until actual_end
            heapq.heappush(busy, (actual_end, room))

        # Determine the room with the most bookings (tie -> smallest index)
        max_bookings = max(count)
        for idx, c in enumerate(count):
            if c == max_bookings:
                return idx

        return -1