# Leetcode 407: Trapping Rain Water II
# https://leetcode.com/problems/trapping-rain-water-ii/
# Solved on 3rd of October, 2025
import heapq


class Solution:
    def trapRainWater(self, heightMap: list[list[int]]) -> int:
        """
        Calculates the amount of rainwater that can be trapped within a 2D height map.

        Args:
            heightMap: A list of lists of integers representing the height of each cell.
        Returns:
            The total amount of rainwater trapped.
        """
        if not heightMap or not heightMap[0]:
            return 0
        m, n = len(heightMap), len(heightMap[0])
        # If the grid is too small to trap water
        if m < 3 or n < 3:
            return 0

        visited = [[False] * n for _ in range(m)]
        heap = []

        # Push all boundary cells into min-heap and mark visited
        for i in range(m):
            for j in (0, n - 1):
                heapq.heappush(heap, (heightMap[i][j], i, j))
                visited[i][j] = True
        for j in range(1, n - 1):
            for i in (0, m - 1):
                heapq.heappush(heap, (heightMap[i][j], i, j))
                visited[i][j] = True

        water_trapped = 0
        # This represents the highest boundary we've seen so far while expanding
        max_seen = -10 ** 9

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while heap:
            height, x, y = heapq.heappop(heap)
            # Update the current maximum boundary height encountered
            if height > max_seen:
                max_seen = height

            # Explore neighbors
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    visited[nx][ny] = True
                    nh = heightMap[nx][ny]
                    # If neighbor is lower than the current max boundary, it can hold water
                    if nh < max_seen:
                        water_trapped += (max_seen - nh)
                        # Push neighbor with effective height = max_seen (water level)
                        heapq.heappush(heap, (max_seen, nx, ny))
                    else:
                        # Neighbor is higher or equal, becomes a new boundary
                        heapq.heappush(heap, (nh, nx, ny))

        return water_trapped