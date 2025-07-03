# Leetcode 2617: Minimum Number of Visited Cells in a Grid
# https://leetcode.com/problems/minimum-number-of-visited-cells-in-a-grid/
# Solved on 3rd of July, 2025
import heapq


class Solution:
    def minimumVisitedcells(self, grid: list[list[int]]) -> int:
        """
        Calculates the minimum number of cells visited to reach the bottom-right cell
        (m-1, n-1) from the top-left cell (0, 0) in a grid.

        You can move from a cell (r, c) to any cell (r, j) where c < j <= c + grid[r][c]
        (moving right) or to any cell (i, c) where r < i <= r + grid[r][c] (moving down).

        Args:
            grid: A 2D list of integers representing the grid. Each cell grid[r][c]
                  contains a non-negative integer indicating the maximum number of steps
                  you can move right or down from that cell.

        Returns:
            The minimum number of cells visited to reach (m-1, n-1).
            Returns -1 if the bottom-right cell is unreachable.
        """
        n, m = len(grid), len(grid[0])
        INF = 10**18
        dist = [[INF] * m for _ in range(n)]
        dist[0][0] = 1

        next_row = [list(range(m + 1)) for _ in range(n)]
        next_col = [list(range(n + 1)) for _ in range(m)]

        def find_row(i: int, x: int) -> int:
            pr = next_row[i]
            if pr[x] != x:
                pr[x] = find_row(i, pr[x])
            return pr[x]

        def find_col(j: int, x: int) -> int:
            pc = next_col[j]
            if pc[x] != x:
                pc[x] = find_col(j, pc[x])
            return pc[x]

        heap = [(1, 0, 0)]
        while heap:
            d, i, j = heapq.heappop(heap)

            if d != dist[i][j]:
                continue

            if (i == (n - 1)) and (j == (m - 1)):
                return d

            k = grid[i][j]
            right_end = min((m - 1), (j + k))
            x = find_row(i, (j + 1))
            while x <= right_end:
                if dist[i][x] > d + 1:
                    dist[i][x] = d + 1
                    heapq.heappush(heap, (d + 1, i, x))

                next_row[i][x] = x + 1
                x = find_row(i, x)

            down_end = min((n - 1), (i + k))
            y = find_col(j, (i + 1))
            while y <= down_end:
                if dist[y][j] > d + 1:
                    dist[y][j] = d + 1
                    heapq.heappush(heap, (d + 1, y, j))

                next_col[j][y] = y + 1
                y = find_col(j, y)

        return -1