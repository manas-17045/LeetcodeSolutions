# Leetcode 1727: Largest Submatrix With Rearrangements
# https://leetcode.com/problems/largest-submatrix-with-rearrangements/
# Solved on 17th of March, 2026
class Solution:
    def largestSubmatrix(self, matrix: list[list[int]]) -> int:
        """
        Calculates the area of the largest submatrix within a binary matrix after
        optimally rearranging the columns.

        :param matrix: A 2D list of integers (0s and 1s).
        :return: The area of the largest submatrix containing only 1s.
        """
        rowCount = len(matrix)
        colCount = len(matrix[0])
        maxArea = 0

        for i in range(rowCount):
            for j in range(colCount):
                if matrix[i][j] != 0 and i > 0:
                    matrix[i][j] += matrix[i-1][j]

            sortedRow = sorted(matrix[i], reverse=True)

            for j in range(colCount):
                maxArea = max(maxArea, sortedRow[j] * (j + 1))

        return maxArea