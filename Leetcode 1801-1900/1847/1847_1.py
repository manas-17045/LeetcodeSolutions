# Leetcode 1847: Closest Room
# https://leetcode.com/problems/closest-room/
# Solved on 27th of July, 2025
import bisect


class Solution:
    def closestRoom(self, rooms: list[list[int]], queries: list[list[int]]) -> list[int]:
        """
        Finds the closest room for each query based on preferred room ID and minimum size.

        Args:
            rooms: A list of rooms, where each room is represented as [room_id, room_size].
            queries: A list of queries, where each query is represented as [preferred_id, min_size].

        Returns:
            A list of integers, where the i-th element is the ID of the closest room for the i-th query, or -1 if no such room exists.
        """

        rooms.sort(key=lambda room: room[1], reverse=True)

        augmentedQueries = []
        for i, query in enumerate(queries):
            augmentedQueries.append([query[0], query[1], i])

        augmentedQueries.sort(key=lambda query: query[1], reverse=True)

        numQueries = len(queries)
        answer = [-1] * numQueries
        availableRoomIds = []
        roomPointer = 0
        numRooms = len(rooms)

        for preferredId, minSize, originalIndex in augmentedQueries:
            while roomPointer < numRooms and rooms[roomPointer][1] >= minSize:
                roomId = rooms[roomPointer][0]
                bisect.insort(availableRoomIds, roomId)
                roomPointer += 1

            if not availableRoomIds:
                continue

            insertionPoint = bisect.bisect_left(availableRoomIds, preferredId)

            bestRoomId = -1
            minDifference = float('inf')

            # Check ceiling candidate (the one at or after the insertion point)
            if insertionPoint < len(availableRoomIds):
                candidateId = availableRoomIds[insertionPoint]
                difference = abs(candidateId - preferredId)
                minDifference = difference
                bestRoomId = candidateId

            # Check floor candidate (the one before the insertion point)
            if insertionPoint > 0:
                candidateId = availableRoomIds[insertionPoint - 1]
                difference = abs(candidateId - preferredId)

                # If difference is smaller, or if it's equal (tie-break with smaller ID)
                if difference <= minDifference:
                    bestRoomId = candidateId

            answer[originalIndex] = bestRoomId

        return answer