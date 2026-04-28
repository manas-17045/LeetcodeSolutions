# Leetcode 3905: Multi Source Flood Fill
# https://leetcode.com/problems/multi-source-slood-fill/
# Solved on 28th of April, 2026
import collections


class Solution:
    def colorGrid(self, n: int, m: int, sources: list[list[int]]) -> list[list[int]]:
        """
        Performs a multi-source flood fill on an n x m grid.

        :param n: Number of rows in the grid.
        :param m: Number of columns in the grid.
        :param sources: A list of [row, col, color] representing the starting points.
        :return: A 2D grid where each cell is filled with the color of the nearest source.
        """
        resultGrid = [[0] * m for _ in range(n)]
        sources.sort(key=lambda x: x[2], reverse=True)
        queue = collections.deque()

        for row, col, color in sources:
            resultGrid[row][col] = color
            queue.append((row, col, color))

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            currentRow, currentCol, currentColor = queue.popleft()

            for rowOffset, colOffset in directions:
                nextRow = currentRow + rowOffset
                nextCol = currentCol + colOffset

                if 0 <= nextRow < n and 0 <= nextCol < m and resultGrid[nextRow][nextCol] == 0:
                    resultGrid[nextRow][nextCol] = currentColor
                    queue.append((nextRow, nextCol, currentColor))

        return resultGrid