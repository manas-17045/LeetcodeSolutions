# Leetcode 3651: Minimum Cost Path with Teleportations
# https://leetcode.com/problems/minimum-cost-path-with-teleportations/
# Solved on 2nd of December, 2025
import heapq
from collections import defaultdict


class Solution:
    def minCost(self, grid: list[list[int]], k: int) -> int:
        """
        Calculates the minimum cost to reach the bottom-right cell (m-1, n-1) from the top-left cell (0, 0)
        in a grid, with the ability to use at most 'k' teleportations.

        Args:
            grid: A 2D list of integers representing the cost to enter each cell.
            k: The maximum number of teleportations allowed.

        Returns:
            The minimum cost to reach the bottom-right cell.
        """
        m, n = len(grid), len(grid[0])
        cellsByVal = defaultdict(list)
        for r in range(m):
            for c in range(n):
                cellsByVal[grid[r][c]].append((r, c))

        sortedVals = sorted(cellsByVal.keys())
        inf = float('inf')
        dist = [[[inf] * n for _ in range(m)] for _ in range(k + 1)]
        dist[0][0][0] = 0

        pq = [(0, 0, 0, 0)]

        processedValIdx = [-1] * (k + 1)

        while pq:
            d, r, c, u = heapq.heappop(pq)

            if d > dist[u][r][c]:
                continue

            if r == m - 1 and c == n - 1:
                return d

            if r + 1 < m:
                nr, nc = r + 1, c
                newCost = d + grid[nr][nc]
                if newCost < dist[u][nr][nc]:
                    dist[u][nr][nc] = newCost
                    heapq.heappush(pq, (newCost, nr, nc, u))

            if c + 1 < n:
                nr, nc = r, c + 1
                newCost = d + grid[nr][nc]
                if newCost < dist[u][nr][nc]:
                    dist[u][nr][nc] = newCost
                    heapq.heappush(pq, (newCost, nr, nc, u))

            if u < k:
                currentVal = grid[r][c]
                idx = processedValIdx[u] + 1

                while idx < len(sortedVals) and sortedVals[idx] <= currentVal:
                    val = sortedVals[idx]
                    for tr, tc in cellsByVal[val]:
                        if d < dist[u + 1][tr][tc]:
                            dist[u + 1][tr][tc] = d
                            heapq.heappush(pq, (d, tr, tc, u + 1))
                    processedValIdx[u] = idx
                    idx += 1

        return -1