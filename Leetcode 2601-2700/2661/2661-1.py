# Leetcode 2661: First Completely Painted Row or Column
# https://leetcode.com/problems/first-completely-painted-row-or-column/
# Solved on 31st of August, 2025
class Solution:
    def firsCompleteIndex(self, arr: list[list[int]], mat: list[list[int]]) -> int:
        """
        Finds the index of the first number in `arr` that completes either a row or a column in `mat`.

        Args:
            arr (list[list[int]]): A list of integers representing the order in which numbers are painted.
            mat (list[list[int]]): A 2D matrix of integers.
        Returns:
            int: The index in `arr` of the first number that completes a row or column in `mat`.
        """
        numRows = len(mat)
        numCols = len(mat[0])

        posMap = {}
        for rowIndex in range(numRows):
            for colIndex in range(numCols):
                posMap[mat[rowIndex][colIndex]] = (rowIndex, colIndex)

        rowCount = [0] * numRows
        colCount = [0] * numCols

        for currentIndex, currentValue in enumerate(arr):
            rowIndex, colIndex = posMap[currentValue]

            rowCount[rowIndex] += 1
            colCount[colIndex] += 1

            if rowCount[rowIndex] == numCols or colCount[colIndex] == numRows:
                return currentIndex

        return -1