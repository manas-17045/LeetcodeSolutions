# Leetcode 778: Swim in Rising Water
# https://leetcode.com/problems/swim-in-rising-water/
# Solved on 6th of October, 2025
import heapq


class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        """
        Finds the least time t such that you can swim from the top-left square (0, 0)
        to the bottom-right square (n-1, n-1) in a grid where grid[r][c] represents
        the elevation at that point. You can only swim from a square (r, c) to a
        neighboring square (dr, dc) if and only if the elevation of both squares
        is at most t.
        :param grid: A 2D list of integers representing the elevation of each square.
        :return: The least time t to swim from (0, 0) to (n-1, n-1).
        """
        n = len(grid)
        minTime = [[float('inf')] * n for _ in range(n)]
        minTime[0][0] = grid[0][0]

        minTime = [(grid[0][0], 0, 0)]

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while minTime:
            time, row, col = heapq.heappop(minTime)

            if time > minTime[row][col]:
                continue

            if row == n - 1 and col == n - 1:
                return time

            for dr, dc in directions:
                newRow = row + dr
                newCol = col + dc

                if 0 <= newRow < n and 0 <= newCol < n:
                    newTime = max(time, grid[newRow][newCol])

                    if newTime < minTime[newRow][newCol]:
                        minTime[newRow][newCol] = newTime
                        heapq.heappush(minTime, (newTime, newRow, newCol))

        return -1