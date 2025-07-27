# Leetcode 1847: Closest Room
# https://leetcode.com/problems/closest-room/
# Solved on 27th of July, 2025
import bisect


class Solution:
    def closestRoom(self, rooms: list[list[int]], queries: list[list[int]]) -> list[int]:
        """
        Finds the closest room ID for each query based on preferred ID and minimum size.

        :param rooms: A list of lists, where each inner list `[id, size]` represents a room.
        :param queries: A list of lists, where each inner list `[preferredId, minSize]` represents a query.
        :return: A list of integers, where each element is the closest room ID for the corresponding query, or -1 if no room satisfies the criteria.
        """

        # Sort rooms by size descending
        rooms.sort(key=lambda x: -x[1])

        # Repackage queries to include original index and sort by minSize descending
        qs = []
        for idx, (preferred, minSize) in enumerate(queries):
            qs.append((minSize, preferred, idx))
        qs.sort(key=lambda x: -x[0])

        ans = [-1] * len(queries)
        available_ids = []  # will hold room IDs, always sorted
        i = 0  # pointer into rooms

        # Process each query in descending order of minSize
        for minSize, preferred, qidx in qs:
            # Add all rooms whose size >= minSize into our "available_ids" set
            while i < len(rooms) and rooms[i][1] >= minSize:
                room_id = rooms[i][0]
                bisect.insort(available_ids, room_id)
                i += 1

            # If no rooms available, answer stays -1
            if not available_ids:
                continue

            # Binary‑search for insertion point of preferred into available_ids
            pos = bisect.bisect_left(available_ids, preferred)

            # Check the candidate at pos (ceiling) and pos-1 (floor), if they exist
            best_id = None
            best_diff = 10 ** 18

            # Ceiling candidate
            if pos < len(available_ids):
                cid = available_ids[pos]
                diff = abs(cid - preferred)
                if diff < best_diff or (diff == best_diff and cid < best_id):
                    best_diff, best_id = diff, cid

            # Floor candidate
            if pos > 0:
                cid = available_ids[pos - 1]
                diff = abs(cid - preferred)
                if diff < best_diff or (diff == best_diff and cid < best_id):
                    best_diff, best_id = diff, cid

            ans[qidx] = best_id

        return ans