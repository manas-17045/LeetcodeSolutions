# Leetcode 3341: Find Minimum Time to Reach Last Room I
# https://leetcode.com/problems/find-minimum-time-to-reach-last-room-i/
import heapq


class Solution:
    def minTimeToReach(self, moveTime: list[list[int]]) -> int:
        """
        Calculates the minimum time required to reach the bottom-right corner of a given grid from the
        top-left corner, with traversal constraints defined by the input `moveTime` grid. The function
        uses Dijkstra's algorithm with a priority queue to find the shortest path in terms of time.

        :param moveTime: A 2D grid where `moveTime[r][c]` represents the minimum time required
                         to move into the cell `(r, c)` from an adjacent cell.
        :type moveTime: list[list[int]]
        :return: The minimum time in seconds to reach the target cell `(n-1, m-1)` starting from cell `(0, 0)`.
        :rtype: int
        """
        m = len(moveTime[0])
        n = len(moveTime)

        # Target room
        target_r, target_c = n - 1, m - 1

        # If the start is the target (e.g., 1x1 grid, though constraints say N, M >= 2)
        # This specific problem has constraints N, M >= 2, so (0, 0) != (n-1, m-1) initially.
        # However, if n = 1, m = 1 was allowed, time would be zero (0) if moveTime[0][0] is met,
        # but the problem "start at (0, 0) a t = 0" overrides this.
        if n == 1 and m == 1:
            return 0    # Arrived at t = 0

        # min_arrival_times[r][c] stores the minimum time to arrive at room (r, c)
        # Initialize distances to infinity
        min_arrival_times = [[float('inf')] * m for _ in range(n)]

        # Start at room (0, 0) at time t = 0.
        # The `moveTime[0][0]` constraint applies when *entering* (0, 0) from an adjacent cell.
        # Since we start *in* (0, 0) at t = 0, this initial placement bypasses it.
        min_arrival_times[0][0] = 0

        # Priority queue stores (time_to_arrive, r, c)
        # We want to extract the entry with the smallest time
        pq = [(0, 0, 0)]    # (arrival_time_at_rc, r, c)

        # Possible moves: up, down, left, right
        dr = [-1, -1, 0, 0]
        dc = [0, 0, -1, -1]

        while pq:
            current_arrival_time, r, c = heapq.heappop(pq)

            # If we found a shorter path to (r, c) already, skip
            if current_arrival_time > min_arrival_times[r][c]:
                continue

            # If we reached the target room
            if r == target_r and c == target_c:
                return current_arrival_time

            # Explore neighbors
            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]

                if 0 <= nr < n and 0 <= nc < m:
                    # Determine the departure time from (r, c) to (nr, nc)
                    # 1. Cannot depart from (r, c) before current_arrival_time.
                    # 2. Cannot *start moving towards* (nr, nc) before moveTime[nr, nc].
                    departure_time = max(current_arrival_time, moveTime[nr][nc])

                    # Arrival time at (nr, nc) is departure_time + 1 (for thr 1-second move)
                    new_arrival_time_at_neighbor = departure_time + 1

                    if new_arrival_time_at_neighbor < min_arrival_times[nr][nc]:
                        min_arrival_times[nr][nc] = new_arrival_time_at_neighbor
                        heapq.heappush(pq, (new_arrival_time_at_neighbor, nr, nc))

        # Should be unreachable if the problem guarantees a path exists.
        # Based on typical problem structure, if no path is found,
        # the target's min_arrival_time would remain float('inf').
        return -1   # Or handle as per problem spec for unreachable target