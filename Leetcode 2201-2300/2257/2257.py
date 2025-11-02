# Leetcode 2257: Count Unguarded Cells in the Grid
# https://leetcode.com/problems/count-unguarded-cells-in-the-grid/
# Solved on 2nd of october, 2025
class Solution:
    def countUnguarded(self, m: int, n: int, guards: list[list[int]], walls: list[list[int]]) -> int:
        """
        Counts the number of unguarded cells in a grid.

        Args:
            m (int): The number of rows in the grid.
            n (int): The number of columns in the grid.
            guards (list[list[int]]): A list of [row, col] coordinates for guards.
            walls (list[list[int]]): A list of [row, col] coordinates for walls.

        Returns:
            int: The number of unguarded cells.
        """
        grid = [[0 for _ in range(n)] for _ in range(m)]

        for r, c in walls:
            grid[r][c] = 2

        for r, c in guards:
            grid[r][c] = 1

        for r, c in guards:
            # North
            for i in range(r - 1, -1, -1):
                cellState = grid[i][c]
                if cellState == 1 or cellState == 2:
                    break
                if cellState == 0:
                    grid[i][c] = 3

            # South
            for i in range(r + 1, m):
                cellState = grid[i][c]
                if cellState == 1 or cellState == 2:
                    break
                if cellState == 0:
                    grid[i][c] = 3

            # West
            for j in range(c - 1, -1, -1):
                cellState = grid[r][j]
                if cellState == 1 or cellState == 2:
                    break
                if cellState == 0:
                    grid[r][j] = 3

            # East
            for j in range(c + 1, n):
                cellState = grid[r][j]
                if cellState == 1 or cellState == 2:
                    break
                if cellState == 0:
                    grid[r][j] = 3

        unguardedCount = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    unguardedCount += 1

        return unguardedCount