# Leetcode 3342: Find Minimum Time to Reach Last Room II
# https://leetcode.com/problems/find-minimum-time-to-reach-last-room-ii/
import heapq


class Solution:
    def minTimeToReach(self, moveTime: list[list[int]]) -> int:
        """
        Calculates the minimum time to traverse from the top-left corner
        to the bottom-right corner of a grid, where each cell represents
        a movement cost.

        The function applies Dijkstra's shortest path algorithm to optimize
        path traversal, accounting for weighted movement costs and parity-based
        movement adjustments. It uses a heap-based priority queue to efficiently
        determine the shortest path across the grid.

        :param moveTime: A 2D list of integers where moveTime[i][j] represents
                         the movement cost associated with cell (i, j).
        :type moveTime: list[list[int]]
        :return: The minimum time required to navigate the grid from the top-left
                 to the bottom-right corner. Returns -1 if the destination
                 is unreachable.
        :rtype: int
        """
        def dijkstra(moveTime, src, dst):
            """
            Provides a solution for calculating the minimum time required to
            move from the top-left corner to the bottom-right corner of a grid,
            given a matrix where each cell has a specific movement cost.

            The algorithm employs Dijkstra's algorithm for finding the shortest
            path on a weighted grid. It ensures the path covers the least possible
            movement time cost, incorporating alternative movement costs based
            on the current cell's parity (row + column position). Each move
            considers four possible directions: up, down, left, and right.

            """
            DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            m, n = len(moveTime), len(moveTime[0])
            dist = [[float('inf')] * n for _ in range(m)]
            dist[0][0] = 0

            # Heap elements are tuples: (distance, (x, y))
            minHeap = [(dist[0][0], src)]

            while minHeap:
                d, (i, j) = heapq.heappop(minHeap)
                if (i, j) == dst:
                    return d
                if d > dist[i][j]:
                    continue
                for dx, dy in DIRS:
                    x, y = i + dx, j + dy
                    if not (0 <= x < m and 0 <= y < n):
                        continue

                    # Movement cost alternates by parity of current position
                    move_cost = (i + j) % 2 + 1
                    newDist = max(moveTime[x][y], d) + move_cost
                    if newDist < dist[x][y]:
                        dist[x][y] = newDist
                        heapq.heappush(minHeap, (newDist, (x, y)))

            return -1

        m, n = len(moveTime), len(moveTime[0])
        return dijkstra(moveTime, (0, 0), (m - 1, n - 1))