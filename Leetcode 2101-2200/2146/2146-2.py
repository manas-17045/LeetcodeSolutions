# Leetcode 2146: K Highest Ranked Items Within a Price Range
# https://leetcode.com/problems/k-highest-ranked-items-within-a-price-range/
# Solved on 13th of September, 2025
import heapq
from collections import deque


class Solution:
    def highestRankedKItems(self, grid: list[list[int]], pricing: list[int], start: list[int], k: int) -> list[list[int]]:
        """
        Finds the k highest-ranked items in a grid based on distance, price, row, and column.

        Args:
            grid: A 2D list representing the grid. 0 means an obstacle, 1 means a wall,
                  and other positive integers represent item prices.
            pricing: A list [low, high] defining the acceptable price range for items.
            start: A list [row, col] indicating the starting position.
            k: The number of highest-ranked items to return.

        Returns:
            A list of lists, where each inner list [row, col] represents the coordinates
            of a highest-ranked item, sorted according to the ranking criteria.
        """
        m = len(grid)
        n = len(grid[0])
        low, high = pricing
        sr, sc = start

        # BFS to find distances to every reachable cell (non-zero)
        q = deque()
        q.append((sr, sc, 0))
        visited = [[False] * n for _ in range(m)]
        visited[sr][sc] = True

        items = []

        while q:
            r, c, d = q.popleft()

            val = grid[r][c]
            # If this cell has an item within the price range, collect it.
            if val != 1 and low <= val <= high:
                items.append((d, val, r, c))

            # Expand neighbors
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc] and grid[nr][nc] != 0:
                    visited[nr][nc] = True
                    q.append((nr, nc, d + 1))

        # If there are no items, return empty list.
        if not items:
            return []

        # If k is small relative to number of items, use nsmallest tio avoid sorting all.
        if k < len(items):
            best = heapq.nsmallest(k, items)
        else:
            items.sort()
            best = items[:k]

        # Return only coordinates in required format
        return [[r, c] for (_, _, r, c) in best]