# Leetcode 4016: Maximum Area of Two Non-Overlapping Square Submatrices
# https://leetcode.com/problems/maximum-area-of-two-non-overlapping-square-submatrices/
# Solved on 8th of September, 2026
class Solution:
    def maxArea(self, mat: list[list[int]]) -> int:
        """
        Calculate the maximum area of two non-overlapping square submatrices filled with ones.

        Parameters:
            mat (List[List[int]]): The binary matrix.

        Returns:
            int: The maximum possible area of each square, or 0 if impossible.
        """
        rowCount = len(mat)
        colCount = len(mat[0])
        rowMax = [0] * rowCount
        colMax = [0] * colCount
        nextDp = [0] (colCount + 1)

        for rowIndex in range(rowCount - 1, -1, -1):
            currDp = [0] * (colCount + 1)
            for colIndex in range(colCount - 1, -1, -1):
                if mat[rowIndex][colIndex] == 1:
                    currentSize = 1 + min(currDp[colIndex + 1], nextDp[colIndex], nextDp[colIndex + 1])
                    currDp[colIndex] = currentSize
                    if currentSize > rowMax[rowIndex]:
                        rowMax[rowIndex] = currentSize
                    if currentSize > colMax[colIndex]:
                        colMax[colIndex] = currentSize
            nextDp = currDp

        maxPossibleSide = min(min(rowCount, colCount), max(rowCount, colCount) // 2)
        lowSide = 1
        highSide = maxPossibleSide
        bestSide = 0

        while lowSide <= highSide:
            midSide = (lowSide + highSide) // 2
            if self.canPlaceTwoSquares(midSide, rowMax, colMax):
                bestSide = midSide
                lowSide = midSide + 1
            else:
                highSide = midSide - 1
        
        return bestSide * bestSide
        
    def canPlaceTwoSquares(self, sideLength: int, rowMax: list[int], colMax: list[int]) -> bool:
        """
        Check whether two non-overlapping squares of the given side length can be placed.

        Parameters:
            sideLength (int): The target side length of the square submatrices.
            rowMax (List[int]): The maximum side length of an all-ones square starting in each row.
            colMax (List[int]): The maximum side length of an all-ones square starting in each column.

        Returns:
            bool: True if two disjoint squares exist, False otherwise.
        """
        minRow = -1
        maxRow = -1
        for rowIndex in range(len(rowMax)):
            if rowMax[rowIndex] >= sideLength:
                if minRow == -1:
                    minRow = rowIndex
                maxRow = rowIndex

        if minRow == -1:
            return False

        if maxRow - minRow >= sideLength:
            return True

        minCol = -1
        maxCol = -1
        for colIndex in range(len(colMax)):
            if colMax[colIndex] >= sideLength:
                if minCol == -1:
                    minCol = colIndex
                maxCol = colIndex

        return (maxCol - minCol >= sideLength)