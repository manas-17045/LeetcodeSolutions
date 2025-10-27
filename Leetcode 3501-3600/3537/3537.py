# Leetcode 3537: Fill a Special Grid
# https://leetcode.com/problems/fill-a-special-grid/
# Solved on 27th of october, 2025
class Solution:
    def specialGrid(self, n: int) -> list[list[int]]:
        """
        Fills a special grid of size 2^n x 2^n according to a specific recursive pattern.

        :param n: An integer representing the level of the grid. The grid will have dimensions 2^n x 2^n.
        :return: A list of lists of integers representing the filled special grid.
        """
        currentGrid = [[0]]

        if n == 0:
            return currentGrid

        for i in range(1, n + 1):
            prevDim = 1 << (i - 1)
            currentDim = 1 << i

            newGrid = [[0] * currentDim for _ in range(currentDim)]

            offsetK = prevDim * prevDim

            trOffset = 0
            brOffset = offsetK
            blOffset = 2 * offsetK
            tlOffset = 3 * offsetK

            for r in range(prevDim):
                for c in range(prevDim):
                    val = currentGrid[r][c]

                    newGrid[r][c] = val + tlOffset
                    newGrid[r][c + prevDim] = val + trOffset
                    newGrid[r + prevDim][c] = val + blOffset
                    newGrid[r + prevDim][c + prevDim] = val + brOffset

            currentGrid = newGrid

        return currentGrid