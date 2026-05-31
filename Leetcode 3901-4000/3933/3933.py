# Leetcode 3933: Largest Local Values in a Matrix II
# https://leetcode.com/problems/largest-local-values-in-a-matrix-ii/
# Solved on 31st of May, 2026
class Solution:
    def countLocalMaximums(self, matrix: list[list[int]]) -> int:
        """
        Calculates the number of local maximums in a matrix based on specific distance criteria.

        :param matrix: A 2D list of integers representing the input matrix.
        :return: An integer representing the total count of local maximums found.
        """
        rowCount = len(matrix)
        colCount = len(matrix[0])
        valueToCells = {}

        for row in range(rowCount):
            for col in range(colCount):
                val = matrix[row][col]
                if val > 0:
                    if val not in valueToCells:
                        valueToCells[val] = []
                    valueToCells[val].append((row, col))

        localMaxCount = 0

        for val, cells in valueToCells.items():
            prefixSum = [[0] * (colCount + 1) for _ in range(rowCount + 1)]
            for row in range(rowCount):
                for col in range(colCount):
                    prefixSum[row + 1][col + 1] = (1 if matrix[row][col] > val else 0) + prefixSum[row + 1][col] + \
                                                  prefixSum[row][col + 1] - prefixSum[row][col]

            for row, col in cells:
                minRow = max(0, row - val)
                maxRow = min(rowCount - 1, row + val)
                minCol = max(0, col - val)
                maxCol = min(colCount - 1, col + val)

                total = prefixSum[maxRow + 1][maxCol + 1] - prefixSum[minRow][maxCol + 1] - prefixSum[maxRow + 1][
                    minCol] + prefixSum[minRow][minCol]

                if row - val >= 0 and col - val >= 0 and matrix[row - val][col - val] > val:
                    total -= 1
                if row - val >= 0 and col + val < colCount and matrix[row - val][col + val] > val:
                    total -= 1
                if row + val < rowCount and col - val >= 0 and matrix[row + val][col - val] > val:
                    total -= 1
                if row + val < rowCount and col + val < colCount and matrix[row + val][col + val] > val:
                    total -= 1

                if total == 0:
                    localMaxCount += 1

        return localMaxCount