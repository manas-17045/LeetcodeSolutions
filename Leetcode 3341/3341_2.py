# Leetcode 3341: Find Minimum Time to Reach Last Room I
# https://leetcode.com/problems/find-minimum-time-to-reach-last-room-i/
from heapq import heappop, heappush
from math import inf


class Solution:
    def minTimeToReach(self, moveTime: list[list[int]]) -> int:
        """
        Calculate the minimum time required to reach the bottom-right corner of a grid
        starting from the top-left corner, where each cell contains a value representing
        the minimum time needed to step into that cell.

        This function employs a priority queue to implement a Dijkstra-like algorithm
        for weighted grid traversal, taking into account the varying costs of traversing
        each cell.

        :param moveTime: A 2D list representing the grid where each cell contains an
                         integer that denotes the minimum time required to step into
                         that cell.
        :type moveTime: list[list[int]]
        :return: The minimum time required to reach the bottom-right corner starting
                 from the top-left corner. Returns -1 if no valid path is possible.
        :rtype: int
        """
        n, m = len(moveTime), len(moveTime[0])  # Get dimensions of the grid
        # Initialize distance grid
        dist = [[inf] * m for _ in range(n)]
        dist[0][0] = 0  # Starting point
        pq = [(0, 0, 0)]    # Priority queue

        # Directions for moving in the grid (up, right, down, left)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while pq:
            current_time, i, j = heappop(pq)    # Get the minimum time node

            # Return the time if we reach the destination
            if (i, j) == (n -1, m - 1):
                return current_time

            # Skip if we've already found a better path
            if current_time > dist[i][j]:
                continue

            # Explore all possible movements
            for dir_x, dir_y in directions:
                x, y = i + dir_x, j + dir_y     # Calculate new coordinates
                # Stay with grid bounds
                if 0 <= x < n and 0 <= y < m:
                    # Calculate the time to reach this new position
                    time_to_reach = max(current_time, moveTime[x][y]) + 1
                    if time_to_reach < dist[x][y]:  # If found a shorter path
                        dist[x][y] = time_to_reach
                        heappush(pq, (time_to_reach, x, y))   # Push new time to queue

        return -1   # If no path is found