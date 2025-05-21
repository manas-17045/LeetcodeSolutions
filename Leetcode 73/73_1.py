# Leetcode 73: Set Matrix Zeroes
# https://leetcode.com/problems/set-matrix-zeroes/
# Solved on 21st of May, 2025

class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n, firstRowHasZero = len(matrix), len(matrix[0]), not all(matrix[0])
        for i in range(1, m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[0][j] = matrix[i][0] = 0
        for i in range(1, m):
            for j in range(n - 1, -1, -1):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if firstRowHasZero:
            matrix[0] = [0] * n