# Leetcode 3342: Find Minimum Time to Reach Last Room II
# https://leetcode.com/problems/find-minimum-time-to-reach-last-room-ii/
import heapq


class Solution:
    def minTimeToReach(self, moveTime: list[list[int]]) -> int:
        """
        Calculates the minimum time required to reach the bottom-right corner of a grid while adhering
        to specific movement constraints. The constraints impose waiting times based on cell values,
        and movement costs alternate between 1 and 2 based on whether the move is odd or even.

        :param moveTime: A 2D list where each entry denotes the earliest time a move can start from
                         the respective cell.
        :type moveTime: list[list[int]]
        :return: The minimum time necessary to reach the bottom-right corner of the grid.
                 Returns -1 if the destination is unreachable.
        :rtype: int
        """
        n = len(moveTime)
        # Constraints: 2 <= n, m <= 750, so n, m will be at least 2.
        # No need to check for n = 0 or m = 0 based on constraints.
        m = len(moveTime[0])

        # dist[r][c][0] stores the minimum time to reach (r, c) having made an even number of moves.
        # dist[r][c][1] stores the minimum time to reach (r, c) having made an odd number of moves.
        # Initialize distances to finity.
        dist = [[[float('inf')] * 2 for _ in range(m)] for _ in range(n)]

        # Priority queue stores tuples: (current_arrival_time, r, c, moves_made_so_far)
        # Python's heapq implements a min-heap
        pq = []

        # Starting conditions:
        # You start at room (0, 0) at time t = 0, having made 0 moves (which is an even count).
        # The `moveTime[r][c]` constraint applies when (r, c) is the destination of a move.
        # Since we start *in* (0, 0), `moveTime[0][0]` does not impose an additional wait
        # for simply being at (0, 0) at t = 0.
        initial_time_at_start_node = 0

        dist[0][0][0] = initial_time_at_start_node
        heapq.heappush(pq, (initial_time_at_start_node, 0, 0, 0))   # (time, r, c, k_moves)

        # Deltas for moving to adjacent cells (up, down, left, right)
        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]

        while pq:
            current_arrival_time, r, c, k_moves = heapq.heappop(pq)

            current_moves_parity = k_moves % 2

            # If we've already found a shorter path to this state (r, c, with this k_moves_paroty), skip.
            if current_arrival_time > dist[r][c][current_moves_parity]:
                continue

            # Explore neighbors
            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]

                # Check if the neighbor is within grid boundaries
                if 0 <= nr < n and 0 <= nc < m:
                    # Determine the actual time we can depart from (r, c) to (nr, nc).
                    # We are at (r, c), arrived at current_arrival_time.
                    # We can only start moving *to* 9nr, nc) if current_time >= moveTime[nr][nc].
                    # If current_arrival_time < moveTime[nr][nc], we must wait at (r, c) until moveTime[nr][nc].
                    actual_departure_time = max(current_arrival_time, moveTime[nr][nc])

                    # Determine the cost of this next move.
                    # The move from (r, c) to (nr, nc) will be the (k_moves + 1)-th move.
                    # Cost is 1 if the (k_moves + 1)-th move is odd-numbered.
                    # Cost is 2 if the (k_moves + 1)-th move is even-numbered.
                    # This is equivalent to: if k_moves (moves to reach current cell) is even, next move cost is 1.

                    # If k_moves is odd, next move cost is 2.
                    if k_moves % 2 == 0:    # Current k_moves is even, so the (k_moves + 1)-th move is odd-numbered.
                        travel_cost = 1
                    else:   # Current k_moves is odd, so the (k_moves + 1)-th move is even-numbered.
                        travel_cost = 2

                    arrival_at_neighbor_t = actual_departure_time + travel_cost

                    next_k_moves = k_moves + 1
                    next_moves_parity = next_k_moves % 2

                    # If this path to (nr, nc) with next_k_moves is shorter:
                    if arrival_at_neighbor_t < dist[nr][nc][next_moves_parity]:
                        dist[nr][nc][next_moves_parity] = arrival_at_neighbor_t
                        heapq.heappush(pq, (arrival_at_neighbor_t, nr, nc, next_k_moves))

        # The result is the minimum time to reach the destination (n - 1, m - 1),
        # considering arrival with either an even or odd number of total moves.
        result_even_final_moves = dist[n - 1][m - 1][0]
        result_odd_final_moves = dist[n - 1][m - 1][1]

        final_result = min(result_even_final_moves, result_odd_final_moves)

        # If the destination is unreachable, final_result will be float('inf').
        # The problem statement implies reachability and asks for an integer time.
        # If unreachability needs a specific return like -1, it would be handled here.
        # Based on typical competitive programming contexts, if not specified, assume reachability
        # or that float('inf') indicates an issue if it were to be returned as an int.
        if final_result == float('inf'):
            return -1   # Or handle as per specific platform requirements for "unreachable"
        # Given problem structure, usually implies it's always reachable.

        return int(final_result)