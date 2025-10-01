# Leetcode 3128: Right Triangles
# https://leetcode.com/problems/right-triangles/
# Solved on 1st of October, 2025
class Solution:
    def numberOfRightTriangles(self, grid: list[list[int]]) -> int:
        """
        Calculates the number of right triangles in a binary grid.
        :param grid: A list of lists of integers representing the binary grid.
        :return: The total number of right triangles.
        """
        m = len(grid)
        n = len(grid[0])

        rowCount = [sum(row) for row in grid]
        colCount = [sum(grid[i][j] for i in range(m)) for j in range(n)]

        result = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    result += (rowCount[i] - 1) * (colCount[j] - 1)

        return result