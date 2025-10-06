# Leetcode 2812: Find the Safest Path in a Grid
# https://leetcode.com/problems/find-the-safest-path-in-a-grid/
# Solved on 6th of October, 2025
import heapq
from collections import deque


class Solution:
    def maximumSafenessFactor(self, grid: list[list[int]]) -> int:
        """
        Calculates the maximum safeness factor of a path from (0,0) to (n-1, n-1) in a grid.
        The safeness factor of a path is the minimum safeness factor of any cell in the path.
        The safeness factor of a cell is its Manhattan distance to the nearest thief.
        :param grid: A 2D list representing the grid, where 1 indicates a thief and 0 an empty cell.
        :return: The maximum safeness factor achievable.
        """
        n = len(grid)

        # Calculate minimum distance to any thief for each cell using multi-source BFS
        dist = [[float('inf')] * n for _ in range(n)]
        queue = deque()

        # Find all thieves and add to queue
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    dist[i][j] = 0
                    queue.append((i, j))

        # Multi-source BFS to compute distances
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and dist[nx][ny] == float('inf'):
                    dist[nx][ny] = dist[x][y] + 1
                    queue.append((nx, ny))

        # Use modified Dijkstra to find path with maximum safeness factor
        pq = [(-dist[0][0], 0, 0)]
        safeness = [[float('-inf')] * n for _ in range(n)]
        safeness[0][0] = dist[0][0]

        while pq:
            neg_safe, x, y = heapq.heappop(pq)
            current_safe = -neg_safe

            # If we reached the destination
            if x == n - 1 and y == n - 1:
                return current_safe

            # Skip if we've already found a better path to this cell
            if current_safe < safeness[x][y]:
                continue

            # Explore neighbors
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n:
                    # The safeness of the new path is the minimum of current safeness and the cell's distance
                    new_safe = min(current_safe, dist[nx][ny])

                    # Only proceed if this path is better
                    if new_safe > safeness[nx][ny]:
                        safeness[nx][ny] = new_safe
                        heapq.heappush(pq, (-new_safe, nx, ny))

        return 0