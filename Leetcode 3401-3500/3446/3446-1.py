# Leetcode 3446: Sort Matrix by Diagonals
# https://leetcode.com/problems/sort-matrix-by-diagonals/
# Solved on 28th of August, 2025
import collections


class Solutions:
    def sortMatrix(self, grid: list[list[int]]) -> list[list[int]]:
        """
        Sorts the elements of a square matrix along its diagonals.
        Diagonals with a non-negative key (row_index - col_index >= 0) are sorted in descending order.
        Diagonals with a negative key (row_index - col_index < 0) are sorted in ascending order.
        :param grid: A list of lists of integers representing the square matrix.
        :return: The modified matrix with elements sorted along its diagonals.
        """
    def sortMatrix(self, grid: list[list[int]]) -> list[list[int]]:

        matrixSize = len(grid)

        diagonals = collections.defaultdict(list)

        for rowIndex in range(matrixSize):
            for colIndex in range(matrixSize):
                diagKey = rowIndex - colIndex
                diagonals[diagKey].append(grid[rowIndex][colIndex])

        for diagKey, elements in diagonals.items():
            if diagKey >= 0:
                elements.sort(reverse=True)
            else:
                elements.sort()

        pointers = collections.defaultdict(int)
        for rowIndex in range(matrixSize):
            for colIndex in range(matrixSize):
                diagKey = rowIndex - colIndex
                sortedValue = diagonals[diagKey][pointers[diagKey]]
                grid[rowIndex][colIndex] = sortedValue
                pointers[diagKey] += 1

        return grid