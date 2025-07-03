# Leetcode 2617: Minimum Number of Visited Cells in a Grid
# https://leetcode.com/problems/minimum-number-of-visited-cells-in-a-grid/
# Solved on 3rd of July, 2025
import heapq


class Solution:
    def minimumVisitedCells(self, grid: list[list[int]]) -> int:
        """
        Calculates the minimum number of cells visited to reach the bottom-right cell
        (n-1, m-1) from the top-left cell (0, 0) in a given grid.

        Args:
            grid: A 2D list of integers where grid[i][j] represents the maximum
                  number of steps that can be taken from cell (i, j) either
                  to the right or downwards.

        Returns:
            The minimum number of cells visited to reach the bottom-right cell.
            Returns -1 if the bottom-right cell is unreachable.
        """
        m = len(grid)
        n = len(grid[0])

        if m == 1 and n == 1:
            return 1

        # Use float('inf') for unreachable cells
        dist = [[float('inf')] * n for _ in range(m)]

        # Heaps for each row and column to find minimum cost predecessors efficiently
        rowPqs = [[] for _ in range(m)]
        colPqs = [[] for _ in range(n)]

        dist[0][0] = 1

        # Initialize heaps with the starting cell's reach
        startVal = grid[0][0]
        if startVal > 0:
            heapq.heappush(rowPqs[0], (1, startVal))
            heapq.heappush(colPqs[0], (1, startVal))

        for r in range(m):
            for c in range(n):
                if r == 0 and c == 0:
                    continue

                # Remove outdated entries from the row's priority queue
                # These are cells whose reach does not extend to the current column.
                while rowPqs[r] and rowPqs[r][0][1] < c:
                    heapq.heappop(rowPqs[r])

                costFromRow = float('inf')
                if rowPqs[r]:
                    costFromRow = rowPqs[r][0][0]

                # Remove outdated entries from the column's priority queue
                # These are cells whose reach does not extend to the current row.
                while colPqs[c] and colPqs[c][0][1] < r:
                    heapq.heappop(colPqs[c])

                costFromCol = float('inf')
                if colPqs[c]:
                    costFromCol = colPqs[c][0][0]

                minPrevCost = min(costFromRow, costFromCol)

                if minPrevCost != float('inf'):
                    currentDist = 1 + minPrevCost
                    dist[r][c] = currentDist

                    val = grid[r][c]
                    if val > 0:
                        reachC = c + val
                        reachR = r + val
                        heapq.heappush(rowPqs[r], (currentDist, reachC))
                        heapq.heappush(colPqs[r], (currentDist, reachR))

        finalDist = dist[m - 1][n - 1]

        if finalDist == float('inf'):
            return -1
        else:
            return int(finalDist)