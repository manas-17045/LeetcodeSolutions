# Leetcode 48: Rotate Image
# https://leetcode.com/problems/rotate-image/
# Solved on 4th of May, 2026
class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Rotates the n x n 2D matrix representing an image by 90 degrees (clockwise) in-place.

        :param matrix: A list of lists of integers representing the image.
        :return: None. The matrix is modified in-place.
        """
        matrixLength = len(matrix)
        for rowIdx in range(matrixLength):
            for colIdx in range(rowIdx + 1, matrixLength):
                matrix[rowIdx][colIdx], matrix[colIdx][rowIdx] = matrix[colIdx][rowIdx], matrix[rowIdx][colIdx]
        for rowIdx in range(matrixLength):
            matrix[rowIdx].reverse()