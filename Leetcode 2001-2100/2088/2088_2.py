# Leetcode 2088: Count Fertile Pyramids in a Land
# https://leetcode.com/problems/count-fertile-pyramids-in-a-land/
# Solved on 20th of August, 2025
class Solution:
    def countPyramids(self, grid: list[list[int]]) -> int:
        """
        Counts the total number of regular and inverse pyramids in a given grid.
        :param grid: A 2D list of integers where 1 represents a valid cell and 0 an invalid cell.
        :return: The total count of pyramids.
        """
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])

        left = [[0] * n for _ in range(m)]
        right = [[0] * n for _ in range(m)]

        for i in range(m):
            run = 0
            for j in range(n):
                if grid[i][j] == 1:
                    run += 1
                else:
                    run = 0
                left[i][j] = run

            run = 0
            for j in range(n - 1, -1, -1):
                if grid[i][j] == 1:
                    run += 1
                else:
                    run = 0
                right[i][j] = run

        res = 0

        # Count regular pyramids (apex at (i, j), pointing down)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                k = 1

                while i + k < m and left[i + k][j] >= (k + 1) and right[i + k][j] >= (k + 1):
                    res += 1

        # Count inverse pyramids (apex at (i, j), pointing up)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                k = 1
                while i - k >= 0 and left[i - k][j] >= (k + 1) and right[i - k][j] >= (k + 1):
                    res += 1
                    k += 1

        return res