# Leetcode 1914: Cyclically Rotating a Grid
# https://lwwtcode.com/problems/cyclically-rotating-a-grid/
# Solved on 9th of May, 2026
class Solution:
    def rotateGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:
        """
        Rotates the layers of a 2D grid cyclically in a counter-clockwise direction k times.

        :param grid: A 2D list of integers representing the m x n grid.
        :param k: The number of times to rotate each layer cyclically.
        :return: The modified grid after performing the rotations.
        """

        rowCount = len(grid)
        colCount = len(grid[0])
        layersCount = min(rowCount, colCount) // 2

        for layerIndex in range(layersCount):
            topRow = [(layerIndex, colIndex) for colIndex in range(layerIndex, colCount - 1 - layerIndex)]
            rightCol = [(rowIndex, colCount - 1 - layerIndex) for rowIndex in
                        range(layerIndex, rowCount - 1 - layerIndex)]
            bottomRow = [(rowCount - 1 - layerIndex, colIndex) for colIndex in
                         range(colCount - 1 - layerIndex, layerIndex, -1)]
            leftCol = [(rowIndex, layerIndex) for rowIndex in range(rowCount - 1 - layerIndex, layerIndex, -1)]

            layerCoords = topRow + rightCol + bottomRow + leftCol
            layerLen = len(layerCoords)
            effectiveK = k % layerLen
            layerVals = [grid[r][c] for r, c in layerCoords]

            for i in range(layerLen):
                r, c = layerCoords[i]
                valIndex = (i + effectiveK) % layerLen
                grid[r][c] = layerVals[valIndex]

        return grid